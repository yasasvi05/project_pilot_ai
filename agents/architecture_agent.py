
from services.gemini_service import ask_gemini

def architecture_agent(problem):

    prompt = f"""
    Design a complete system architecture for:

    {problem}

    Include:

    1. Frontend
    2. Backend
    3. Database
    4. APIs
    5. AI Components
    6. Deployment
    """

    return ask_gemini(prompt)