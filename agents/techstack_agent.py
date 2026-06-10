from services.gemini_service import ask_gemini

def techstack_agent(problem):

    prompt = f"""
    Recommend the best tech stack for:

    {problem}

    Explain why each technology should be used.
    """

    return ask_gemini(prompt)