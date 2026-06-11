from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from agents.research_agent import research_agent
from agents.architecture_agent import architecture_agent
from agents.techstack_agent import techstack_agent
from agents.planner_agent import planner_agent

from services.pdf_service import extract_text_from_pdf
from services.chroma_service import store_document

app = FastAPI()


class ProjectInput(BaseModel):
    idea: str


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    pdf_path = f"uploads/{file.filename}"

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(pdf_path)

    store_document(
        file.filename,
        text
    )

    return {
        "message": "PDF uploaded and stored successfully"
    }


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