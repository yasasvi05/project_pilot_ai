import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="ProjectPilot AI",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🚀 ProjectPilot AI")

    st.markdown("---")

    st.markdown("### Features")

    st.markdown("""
    ✅ PDF Analysis

    ✅ Multi-Agent AI

    ✅ RAG + ChromaDB

    ✅ Tech Stack Recommendation

    ✅ Development Roadmaps
    """)

    st.markdown("---")

    st.info(
        "Upload a project problem statement and let AI generate architecture, tech stack, and implementation plans."
    )

# Hero Section
st.title("🚀 ProjectPilot AI")

st.markdown("""
### Your AI-Powered Project Mentor

Transform project ideas and problem statements into:

- 📄 Research Analysis
- 🏗️ System Architecture
- ⚙️ Technology Recommendations
- 🗺️ Development Roadmaps

Powered by Gemini, RAG, and ChromaDB.
""")

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.success("📄 Analyze PDFs")

with col2:
    st.success("🧠 AI Agents")

with col3:
    st.success("⚡ Generate Roadmaps")

st.markdown("---")

# PDF Upload
st.subheader("📤 Upload Problem Statement")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    upload_response = requests.post(
        "http://127.0.0.1:8000/upload-pdf",
        files=files
    )

    if upload_response.status_code == 200:
        st.success("✅ PDF Uploaded Successfully!")
    else:
        st.error("❌ PDF Upload Failed")

st.markdown("---")

# Project Idea Input
st.subheader("💡 Enter Your Project Idea")

idea = st.text_area(
    "",
    placeholder="Example: Smart Waste Management System for Colleges",
    height=150
)

# Analyze Button
if st.button(
    "🚀 Analyze Project",
    use_container_width=True
):

    with st.spinner(
        "🤖 AI Agents are analyzing your project..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"idea": idea}
        )

        result = response.json()

    st.success("Analysis Complete!")

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Difficulty", "Medium")

    with col2:
        st.metric("Timeline", "4 Weeks")

    with col3:
        st.metric("AI Agents", "4")

    st.markdown("---")

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Research",
            "🏗️ Architecture",
            "⚙️ Tech Stack",
            "🗺️ Roadmap"
        ]
    )

    with tab1:
        st.write(result["research"])

    with tab2:
        st.write(result["architecture"])

    with tab3:
        st.write(result["techstack"])

    with tab4:
        st.write(result["roadmap"])