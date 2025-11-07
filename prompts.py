# prompts.py
CATEGORIES = {
    "Environmental": ["trash", "litter", "pollution", "green", "climate"],
    "Safety": ["accident", "security", "health", "damage"],
    "Community": ["community", "behavior", "public", "residents"],
    "Infrastructure": ["bench", "repair", "maintenance", "broken"],
    "Other": []
}

CRITICAL_THINKING_PROMPTS = [
    "What causes this? Neglect, materials, habits?",
    "How to confirm it matters? Survey 3-5 people.",
    "Strategies? Replace, repair, redesign?",
    "Zero funds impact? Brainstorm reuse, partnerships.",
    "Surprises during implementation?"
]

QUICK_BUILD_PROMPTS = [
    "Milestone plan: Research, support, execute, measure.",
    "Adaptive budget: Materials, donations.",
    "Tools for prototype: No-code, reuse items.",
    "Document: Photos, videos, challenge log."
]

PERSONALITIES = {
    "Encouraging Coach": {"style": "friendly", "prefix": "Great! ", "suffix": " Keep going!"},
    "Strict Analyst": {"style": "analytical", "prefix": "Evaluate: ", "suffix": " Be precise."}
}

REFLECTION_PROMPTS = [
    "Why this solution?",
    "Differently next time?"
]

# Artifact Templates
PROBLEM_ANALYSIS_MAP = "Problem Analysis Map\n- Causes: {causes}\n- Categories: {categories}"
COMMUNITY_VALIDATION = "Validation Summary\n- Quotes: {quotes}\n- Sentiment: {sentiment}%"
DECISION_LOG = "Decision Log\n- Options: {options}\n- Chosen: {chosen} (Why: {why})"
ADAPTIVE_BUDGET = "Budget Plan\n- Item: {item} (Rationale: {rationale})"
CHALLENGE_LOG = "Challenge vs Solution Log\n- Challenge: {challenge}\n- Solution: {solution}"
IMPACT_REPORT = "Impact Report\n- Metrics: {metrics}\n- Narratives: {narratives}"
REFLECTION_SUMMARY = "Reflection Summary\n- Learnings: {learnings}\n- Badge: {badge}\n- XP: {xp}"
MINI_DECK = "Mini Deck\n- Problem: {problem}\n- Plan: {plan}\n- Impact: {impact}"
MARKET_DISCOVERY = "Market Discovery Report\n- Responses: {responses}\n- Sentiment: {sentiment}%"