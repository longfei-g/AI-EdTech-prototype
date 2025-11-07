from transformers import pipeline
from prompts import CRITICAL_THINKING_PROMPTS, QUICK_BUILD_PROMPTS, PERSONALITIES, COMMUNITY_VALIDATION, DECISION_LOG, ADAPTIVE_BUDGET, CHALLENGE_LOG
import random

generator = pipeline("text-generation", model="gpt2")

def get_mentor_response(mission: str, category: str, user_input: str, personality: str, history: list, mode: str = "Critical Thinking"):
    pers = PERSONALITIES.get(personality, PERSONALITIES["Encouraging Coach"])
    prompts = CRITICAL_THINKING_PROMPTS if mode == "Critical Thinking" else QUICK_BUILD_PROMPTS
    system_prompt = f"AI Mentor ({mode} Mode): Guide on '{mission}' ({category}). Respond with one prompt/suggestion."
    context = "\n".join(history) + f"\nUser: {user_input}"
    base_prompt = random.choice(prompts)
    full_prompt = f"{system_prompt}\n{context}\nMentor: {pers['prefix']}{base_prompt}{pers['suffix']}"
    response = generator(full_prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text'].split("Mentor:")[-1].strip()
    # Generate artifact based on input
    artifact = ""
    if "survey" in user_input.lower() or "validate" in user_input.lower():
        artifact = COMMUNITY_VALIDATION.format(quotes="Sample quotes", sentiment=random.randint(60, 90))
    elif "strategy" in user_input.lower() or "plan" in user_input.lower():
        artifact = DECISION_LOG.format(options="Replace/Repair/Redesign", chosen="Repair", why="Sustainable")
    elif "budget" in user_input.lower() or "resources" in user_input.lower():
        artifact = ADAPTIVE_BUDGET.format(item="Materials", rationale="Reuse for low cost")
    elif "challenge" in user_input.lower() or "execution" in user_input.lower():
        artifact = CHALLENGE_LOG.format(challenge="Unexpected issue", solution="Adapted plan")
    return response + ("\n\nGenerated Artifact:\n" + artifact if artifact else "")