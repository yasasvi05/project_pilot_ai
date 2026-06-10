from fastapi import FastAPI
from pydantic import BaseModel

from agents.research_agent import research_agent
from agents.architecture_agent import architecture_agent
from agents.techstack_agent import techstack_agent
from agents.planner_agent import planner_agent

app = FastAPI()

class ProjectInput(BaseModel):
    idea: str

@app.post("/analyze")
def analyze_project(data: ProjectInput):

    research = research_agent(data.idea)

    architecture = architecture_agent(data.idea)

    techstack = techstack_agent(data.idea)

    roadmap = planner_agent(data.idea)

    return {
        "research": research,
        "architecture": architecture,
        "techstack": techstack,
        "roadmap": roadmap
    }