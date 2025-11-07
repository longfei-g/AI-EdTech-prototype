# problem_engine.py
from transformers import CLIPProcessor, CLIPModel, pipeline
from PIL import Image
from sdg_utils import rule_based_category, get_sdg_match
from prompts import PROBLEM_ANALYSIS_MAP, CATEGORIES

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def identify_problem(text: str = None, image_path: str = None) -> dict:
    if text is None:
        text = ""
    candidate_labels = [f"A photo of {kw}" for cat in CATEGORIES for kw in CATEGORIES[cat]]
    category = rule_based_category(text)
    if image_path:
        image = Image.open(image_path)
        inputs = processor(text=candidate_labels + [text], images=image, return_tensors="pt", padding=True)
        outputs = model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1)[0]
        top_idx = probs.argmax().item()
        fusion_label = candidate_labels[top_idx] if top_idx < len(candidate_labels) else text
        category = rule_based_category(fusion_label) or category
    mission = summarizer(f"Convert to mission for {category}: {text}", max_length=50, min_length=20)[0]['summary_text']
    analysis_map = PROBLEM_ANALYSIS_MAP.format(causes="Neglect, habits (from AI analysis)", categories=category)
    sdg = get_sdg_match(category)
    image_label = "trash" if "trash" in text.lower() or "litter" in text.lower() else "clean" if "clean" in text.lower() else "broken" if "broken" in text.lower() else ""
    return {"mission": mission, "category": category, "sdg": sdg, "analysis_map": analysis_map, "image_label": image_label}