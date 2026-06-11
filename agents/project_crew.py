from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

def run_project_crew(project_idea):

    research_agent = Agent(
        role="Research Analyst",
        goal="Analyze project ideas and identify opportunities",
        backstory="Expert in research and project analysis",
        llm=gemini_llm,
        verbose=True
    )

    architecture_agent = Agent(
        role="System Architect",
        goal="Design scalable system architectures",
        backstory="Expert software architect",
        llm=gemini_llm,
        verbose=True
    )

    techstack_agent = Agent(
        role="Technology Consultant",
        goal="Recommend the best technologies",
        backstory="Expert in modern software stacks",
        llm=gemini_llm,
        verbose=True
    )

    planner_agent = Agent(
        role="Project Planner",
        goal="Create implementation roadmaps",
        backstory="Experienced project manager",
        llm=gemini_llm,
        verbose=True
    )

    research_task = Task(
        description=f"""
        Analyze the following project:

        {project_idea}

        Provide:
        - Problem Summary
        - Key Challenges
        - Opportunities
        """,
        expected_output="""
        A detailed analysis containing:
        - Problem Summary
        - Key Challenges
        - Opportunities
        """,
        agent=research_agent
    )

    architecture_task = Task(
        description=f"""
        Design a complete architecture for:

        {project_idea}

        Include:
        - Frontend
        - Backend
        - Database
        - APIs
        - Deployment
        """,
        expected_output="""
        Complete architecture design document.
        """,
        agent=architecture_agent
    )

    techstack_task = Task(
        description=f"""
        Recommend the best tech stack for:

        {project_idea}
        """,
        expected_output="""
        Recommended technologies with explanations.
        """,
        agent=techstack_agent
    )

    planner_task = Task(
        description=f"""
        Create a 4-week implementation roadmap for:

        {project_idea}
        """,
        expected_output="""
        Week-by-week roadmap.
        """,
        agent=planner_agent
    )

    crew = Crew(
        agents=[
            research_agent,
            architecture_agent,
            techstack_agent,
            planner_agent
        ],
        tasks=[
            research_task,
            architecture_task,
            techstack_task,
            planner_task
        ],
        verbose=True
    )

    result = crew.kickoff()

    return str(result)