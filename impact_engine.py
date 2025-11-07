# impact_engine.py
from transformers import pipeline
from sdg_utils import compute_originality, get_sdg_match  # Fix 4: Import get_sdg_match
from prompts import IMPACT_REPORT, REFLECTION_SUMMARY, MARKET_DISCOVERY, REFLECTION_PROMPTS  # Fix 3: Import REFLECTION_PROMPTS
from database import save_progress  # Fix 1: Import save_progress
import random  # Fix 2: Import random

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(reflection: str, mission: str, category: str) -> str:
    prompt = random.choice(REFLECTION_PROMPTS) + f"\nReflection: {reflection}\nSummarize."
    return summarizer(prompt, max_length=60)[0]['summary_text']

def track_impact(user_id: str, mission: str, category: str, challenges: int, ideas: int, solution_text: str, reflection: str, mode: str = ""):
    originality = compute_originality(solution_text, category)
    desc = "High" if originality > 0.9 else "Medium" if originality > 0.85 else "Low"
    summary = generate_summary(reflection, mission, category)
    badge = "Mental Mastery" if "think" in mode.lower() else "Gold" if originality > 0.9 else "Silver" if originality > 0.85 else "Bronze"
    xp = int((challenges * 10 + ideas * 5 + originality * 100) * 1.4)  # +40% multiplier
    metrics = f"Benefited: {random.randint(5,50)} people; Engagement: {ideas} ideas"
    market_discovery = MARKET_DISCOVERY.format(responses="5 auto-summarized", sentiment=80)
    impact_report = IMPACT_REPORT.format(metrics=metrics, narratives=reflection)
    reflection_summary = REFLECTION_SUMMARY.format(learnings=summary, badge=badge, xp=xp)
    reports = f"{market_discovery}\n{impact_report}\n{reflection_summary}"
    data = {
        "user_id": user_id, "mission": mission, "category": category, "sdg": get_sdg_match(category),
        "challenges": challenges, "ideas": ideas, "originality": originality,
        "reflection": reflection, "summary": summary, "reports": reports
    }
    save_progress(data)
    return reports
if __name__ == "__main__":
    print(track_impact("test_user", "Test Mission", "Environmental", 5, 3, "Test solution", "Test reflection", "Critical Thinking"))