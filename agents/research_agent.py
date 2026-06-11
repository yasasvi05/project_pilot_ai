from services.gemini_service import ask_gemini
from services.chroma_service import retrieve_documents

def research_agent(problem_statement):

    docs = retrieve_documents(problem_statement)

    context = "\n".join(docs)

    prompt = f"""
    You are a Research Analyst.

    Use the following PDF context if relevant.

    Context:
    {context}

    Project:
    {problem_statement}

    Provide:

    1. Problem Summary
    2. Key Challenges
    3. Opportunities
    """

    return ask_gemini(prompt)