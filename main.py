import streamlit as st
import os
import pandas as pd
from database import init_db, get_progress
from problem_engine import identify_problem
from mentor_engine import get_mentor_response
from impact_engine import track_impact
from prompts import PERSONALITIES

init_db()

st.set_page_config(page_title="Fix My World MVP", layout="wide")
st.title("Fix My World: AI EdTech Prototype")

user_id = st.sidebar.text_input("User ID", "demo_user")
project_mode = st.sidebar.selectbox("Mode", ["Student Level", "Teacher/Group"])
project_type = st.sidebar.selectbox("Project Type", ["Hands-on Project", "Community Development"])

tab1, tab2, tab3 = st.tabs(["1. Problem Identification", "2. AI Mentor Guidance", "3. Impact Tracking"])

with tab1:
    st.header("Problem Identification (Sprint 1-3)")
    text = st.text_area("Describe the problem (1-2 sentences)")
    uploaded_file = st.file_uploader("Upload image (optional)", type=["jpg", "png"])
    image_path = None
    if uploaded_file:
        os.makedirs("temp", exist_ok=True)
        image_path = f"temp/{uploaded_file.name}"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded Image")
    if st.button("Analyze Problem"):
        result = identify_problem(text, image_path)
        st.session_state['mission'] = result['mission']
        st.session_state['category'] = result['category']
        st.json(result)
        st.success(f"Mission: {result['mission']}\nCategory: {result['category']}")
        st.markdown(result['analysis_map'])

with tab2:
    st.header("AI Mentor Guidance (Sprints 4-9)")
    if 'mission' not in st.session_state:
        st.info("Identify a problem first.")
    else:
        guidance_mode = st.selectbox("Guidance Mode", ["Critical Thinking (Think Like a Founder)", "Quick Build"])
        personality = st.selectbox("Mentor Personality", list(PERSONALITIES.keys()))
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        for msg in st.session_state.chat_history:
            st.chat_message(msg["role"]).markdown(msg["content"])
        user_input = st.chat_input("Your response or upload (e.g., survey notes, photos):")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            response = get_mentor_response(
                st.session_state['mission'], st.session_state['category'], user_input, personality,
                [f"{m['role']}: {m['content']}" for m in st.session_state.chat_history[:-1]],
                guidance_mode.split(" ")[0]  # Extract mode
            )
            st.session_state.chat_history.append({"role": "mentor", "content": response})
            st.rerun()

with tab3:
    st.header("Impact Tracking & Reflection (Sprint 10)")
    if 'mission' not in st.session_state:
        st.info("Complete previous steps.")
    else:
        solution_text = st.text_area("Solution Ideas/Execution Notes (from mentor chat)")
        reflection = st.text_area("Reflection (e.g., Why this solution? What next?)")
        challenges = st.number_input("Challenges Completed", min_value=0, value=0)
        ideas = st.number_input("Ideas Posted/Implemented", min_value=0, value=0)
        if st.button("Track Impact & Generate Reports"):
            report = track_impact(user_id, st.session_state['mission'], st.session_state['category'],
                                  challenges, ideas, solution_text, reflection)
            st.markdown(report)
        st.subheader("Mock Dashboard (Mentor/Teacher View)")
        progress = get_progress(user_id)
        if progress:
            df = pd.DataFrame(progress, columns=["user_id", "mission", "category", "sdg", "challenges", "ideas", "originality", "reflection", "summary", "timestamp", "reports"])
            st.dataframe(df)
            st.bar_chart(df[["challenges", "ideas", "originality"]])
            for row in df['reports']:
                st.markdown(row)
        else:
            st.info("No progress data yet.")