from services.gemini_service import ask_gemini
from services.chroma_service import retrieve_documents

def techstack_agent(problem):

    docs = retrieve_documents(problem)

    context = "\n".join(docs)

    prompt = f"""
    You are a Technology Consultant.

    Use the following context from uploaded documents if relevant.

    Context:
    {context}

    Project:
    {problem}

    Recommend:

    1. Frontend
    2. Backend
    3. Database
    4. AI/ML Tools
    5. Deployment

    Explain why each technology should be used.
    """

    return ask_gemini(prompt)