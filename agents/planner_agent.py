from services.gemini_service import ask_gemini

def planner_agent(problem):

    prompt = f"""
    Create a 4-week development roadmap for:

    {problem}

    Break work week by week.
    """

    return ask_gemini(prompt)