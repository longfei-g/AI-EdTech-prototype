from transformers import CLIPProcessor, CLIPModel, pipeline
from PIL import Image
from sdg_utils import rule_based_category, get_sdg_match
from prompts import CATEGORIES, PROBLEM_ANALYSIS_MAP

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def identify_problem(text: str = None, image_path: str = None) -> dict:
    candidate_labels = [f"A photo of {kw}" for cat in CATEGORIES for kw in CATEGORIES[cat]]
    category = "Other"
    image_label = ""
    if image_path and text:
        image = Image.open(image_path)
        inputs = processor(text=candidate_labels + [text], images=image, return_tensors="pt", padding=True)
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)[0]
        top_idx = probs.argmax().item()
        if top_idx < len(candidate_labels):
            image_label = candidate_labels[top_idx].replace("A photo of ", "")
            category = next(cat for cat, kws in CATEGORIES.items() if image_label in kws)
    elif text:
        category = rule_based_category(text)
    mission = summarizer(f"Convert to structured mission statement: {text}", max_length=50, min_length=20, do_sample=False)[0]['summary_text']
    analysis_map = PROBLEM_ANALYSIS_MAP.format(causes="Neglect, habits (from AI analysis)", categories=category)
    sdg = get_sdg_match(category)
    return {"mission": mission, "category": category, "analysis_map": analysis_map, "image_label": image_label, "sdg": sdg}