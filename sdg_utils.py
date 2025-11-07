import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from prompts import CATEGORIES

DATASET_PATH = "osdg-community-data-v2024-01-01.csv"

SDG_MAP = {
    "Environmental": "SDG 13/14/15 (Climate/Life Below Water/Life on Land)",
    "Safety": "SDG 3/11 (Health/Sustainable Cities)",
    "Community": "SDG 10/16 (Reduced Inequalities/Peace)",
    "Infrastructure": "SDG 9/11 (Industry/Innovation, Sustainable Cities)",
    "Other": "Other SDG"
}

def load_sdg_data():
    try:
        df = pd.read_csv(DATASET_PATH, sep='\t')
        return df[df['agreement'] > 0.8]
    except FileNotFoundError:
        return pd.DataFrame()

def rule_based_category(text: str) -> str:
    text_lower = text.lower()
    for cat, keywords in CATEGORIES.items():
        if any(kw in text_lower for kw in keywords):
            return cat
    return "Other"

def get_sdg_match(category: str) -> str:
    return SDG_MAP.get(category, "Other SDG")

def compute_originality(solution_text: str, category: str) -> float:
    df = load_sdg_data()
    if df.empty:
        return 0.8
    sdg = get_sdg_match(category).split(" (")[0]
    samples = df[df['sdg'].str.contains(sdg, na=False)]['text'].tolist()[:10]
    if not samples:
        return 0.8
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([solution_text] + samples)
    sims = cosine_similarity(vectors[0:1], vectors[1:])[0].mean()
    return 1 - sims