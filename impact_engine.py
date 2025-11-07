from database import save_progress
from transformers import pipeline
from sdg_utils import compute_originality, get_sdg_match
from prompts import IMPACT_REPORT, REFLECTION_PROMPTS, REFLECTION_SUMMARY, MINI_DECK
import random

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(reflection: str, mission: str, category: str) -> str:
    prompt = random.choice(REFLECTION_PROMPTS) + f"\nReflection: {reflection}\nSummarize learnings and impact."
    return summarizer(prompt, max_length=60, min_length=30, do_sample=False)[0]['summary_text']

def track_impact(user_id: str, mission: str, category: str, challenges: int, ideas: int, solution_text: str, reflection: str):
    originality = compute_originality(solution_text, category)
    innovation_desc = "High" if originality > 0.9 else "Medium" if originality > 0.85 else "Low"
    badge = "Mental Mastery" if "thinking" in reflection.lower() else "Bronze Badge"
    xp = int((challenges + ideas) * 10 + originality * 100) * 1.4  # +40% for effort/originality
    summary = generate_summary(reflection, mission, category)
    mini_deck = MINI_DECK.format(problem=mission, plan=solution_text, impact=f"Challenges: {challenges}, Ideas: {ideas}")
    impact_report = IMPACT_REPORT.format(metrics=f"Benefited {random.randint(5,50)} people", narratives=summary)
    reflection_summary = REFLECTION_SUMMARY.format(learnings=summary, badge=badge, xp=xp)
    full_report = f"{mini_deck}\n\n{impact_report}\n\n{reflection_summary}"
    data = {
        "user_id": user_id, "mission": mission, "category": category, "sdg": get_sdg_match(category),
        "challenges": challenges, "ideas": ideas, "originality": originality,
        "reflection": reflection, "summary": summary, "reports": full_report
    }
    save_progress(data)
    return full_report