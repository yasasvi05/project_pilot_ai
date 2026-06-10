from services.gemini_service import ask_gemini

def research_agent(problem_statement):

    prompt = f"""
    Analyze the following project idea.

    Project:
    {problem_statement}

    Give:
    1. Problem Summary
    2. Key Challenges
    3. Opportunities
    """

    return ask_gemini(prompt)