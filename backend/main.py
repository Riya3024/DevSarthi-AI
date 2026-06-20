from fastapi import FastAPI
from pydantic import BaseModel

from agent.graph import agent
from project_brain import router as brain_router



from timeline import router as timeline_router


app = FastAPI()

app.include_router(brain_router)
app.include_router(timeline_router)

class Query(BaseModel):
    message: str
    repo_url: str | None = None



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
        "answer": result.get("response", "No response generated"),
        "analysis": result.get("analysis", {}),
        "memory": result.get("memory", [])
    }