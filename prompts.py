# prompts.py
# Categories from examples (Environmental, Safety, Community, Infrastructure, etc.)
CATEGORIES = {
    "Environmental": ["trash", "litter", "pollution", "green", "climate"],
    "Safety": ["accident", "security", "health", "damage"],
    "Community": ["community", "behavior", "public", "residents"],
    "Infrastructure": ["bench", "repair", "maintenance", "broken"],
    "Other": []
}

# Critical Thinking prompts (inquiry-driven from examples)
CRITICAL_THINKING_PROMPTS = [
    "What do you think causes this issue? Is it neglect, materials, or habits?",
    "How can we confirm this matters to others? Survey 3-5 people.",
    "Before fixing, what strategies exist? Replace? Repair? Redesign?",
    "If you had zero funds, how would you make an impact?",
    "What surprised you during implementation?"
]

# Quick Build prompts (action-oriented)
QUICK_BUILD_PROMPTS = [
    "Outline steps for a hands-on project: Research, Gather Support, Execute.",
    "Create an adaptive budget: Materials, partnerships, donations.",
    "Suggest quick tools for prototyping: Reuse items, simple plans.",
    "How to document execution: Photos, videos, challenges log."
]

# Personalities unchanged

# Reflection prompts
REFLECTION_PROMPTS = [
    "Why did you choose this solution?",
    "If you were city planners, what would you do differently?"
]

# Report templates (from examples)
MARKET_DISCOVERY_TEMPLATE = """
Market Discovery Report
- Survey Responses: {responses}
- Sentiment: {sentiment}% positive
"""

MINI_DECK_TEMPLATE = """
Mini Business Deck
- Problem: {problem}
- Plan: {plan}
- Impact: {impact}
"""

IMPACT_SUMMARY_TEMPLATE = """
Impact Summary
- Metrics: {metrics}
- Score: {score}
- Innovation: {innovation}
"""

REFLECTION_SUMMARY_TEMPLATE = """
Reflection Summary
- Learnings: {learnings}
- Badge: {badge}
- XP: {xp}
"""