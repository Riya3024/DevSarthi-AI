from fastapi import FastAPI
from pydantic import BaseModel

from agent.graph import agent
from project_brain import router as brain_router
from timeline import router as timeline_router
from health import router as health_router

from fastapi.middleware.cors import CORSMiddleware

from activity import router as activity_router


app = FastAPI()





app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "https://abe0233cd6d843b7a3b6c1d7044cab0c.prod.enterapp.pro",
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(brain_router)
app.include_router(timeline_router)
app.include_router(health_router)
app.include_router(activity_router)



class Query(BaseModel):
    message: str
    repo_url: str | None = None



@app.get("/")
def home():

    return {
        "project": "DevSarthi AI",
        "status": "running",
        "features": [
            "Parcle Persistent Memory",
            "Enter Pro Agent Execution",
            "Architecture Conflict Detection",
            "Engineering Timeline",
            "Documentation Agent"
        ],
        "endpoints": {
            "chat": "/chat",
            "timeline": "/timeline"
        }
    }



@app.post("/chat")
def chat(query: Query):

    result = agent.invoke(
        {
            "user_query": query.message,
            "repo_url": query.repo_url,
            "memory": [],
            "response": "",
            "analysis": {}
        }
    )


    print("AGENT RESULT:", result)


    return {

        "answer": result.get("response"),

        "analysis": result.get("analysis"),

        "memory": result.get("memory"),

        "conflict": result.get(
            "conflict_report",
            "No conflict detected"
        ),

        "execution": result.get(
            "code_changes",
            []
        )
    }



@app.get("/chat")
def chat_info():

    return {
        "message": "Chat API is running",
        "method": "POST",
        "endpoint": "/chat"
    }