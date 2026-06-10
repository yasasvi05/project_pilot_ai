import streamlit as st
import requests

st.title("ProjectPilot AI")

idea = st.text_area("Enter Project Idea")

if st.button("Analyze"):

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={"idea": idea}
    )

    result = response.json()

    st.subheader("Research Analysis")
    st.write(result["research"])

    st.subheader("Architecture")
    st.write(result["architecture"])

    st.subheader("Tech Stack")
    st.write(result["techstack"])

    st.subheader("Roadmap")
    st.write(result["roadmap"])