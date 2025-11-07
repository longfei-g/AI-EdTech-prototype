# EdTech AI Prototype: Fix My World MVP

Core AI for EdTech platform integrating MVSS. Handles problem ID (text/image), mentor guidance (Critical/Quick modes), impact tracking (reports/badges/XP).

## Setup
1. Download OSDG-CD CSV to root (Zenodo: https://zenodo.org/records/10579179).
2. `pip install -r requirements.txt`
3. `streamlit run main.py`

## Features
- CLIP fusion for image+text analysis.
- Mentor modes with artifact generation (e.g., Decision Log).
- Tracking with originality, reflections, badges (Mental Mastery), XP (+40% for effort).
- English UI; SDG-aligned.
- Outputs match examples (e.g., Problem Analysis Map, Impact Report).

## Reproducibility
- Env: Python 3.12+.
- Test with: Text "We don’t have enough bins", image of trash.
- Limitations: Lite models; scale with fine-tuning.

## Collaboration
- Plug Education team: Update prompts.py with taxonomy/scripts.
- UVA UI: Replace text badges with images in impact_engine.py.