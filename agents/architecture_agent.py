from services.gemini_service import ask_gemini
from services.chroma_service import retrieve_documents

def architecture_agent(problem):

    docs = retrieve_documents(problem)

    context = "\n".join(docs)

    prompt = f"""
    You are a System Architect.

    Use the following PDF context if relevant.

    Context:
    {context}

    Project:
    {problem}

    Design a complete architecture.

    Include:

    1. Frontend
    2. Backend
    3. Database
    4. APIs
    5. AI Components
    6. Deployment
    """

    return ask_gemini(prompt)