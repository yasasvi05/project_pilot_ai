from services.chroma_service import retrieve_documents
from services.gemini_service import ask_gemini


def rag_answer(query):

    docs = retrieve_documents(query)

    context = "\n".join(docs)

    prompt = f"""
    Context:
    {context}

    Question:
    {query}

    Answer based only on the context.
    """

    return ask_gemini(prompt)