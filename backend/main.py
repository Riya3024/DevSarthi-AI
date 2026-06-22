from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from agent.graph import agent
from project_brain import router as brain_router
from timeline import router as timeline_router
from health import router as health_router
from activity import router as activity_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


# Routers
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



@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc)
        }
    )



@app.post("/chat")
def chat(query: Query):

    try:

        result = agent.invoke(
            {
                "user_query": query.message,
                "repo_url": query.repo_url,
                "memory": [],
                "response": "",
                "analysis": {}
            }
        )


        print("AGENT RESULT:")
        print(result)


        answer = (
    result.get("response")
    or result.get("output")
    or result.get("final_answer")
    or result.get("answer")
    or result.get("messages")
)


        if isinstance(answer, list):
          

          last = answer[-1]

          if hasattr(last, "content"):
            answer = last.content

          elif isinstance(last, dict):
            answer = (
            last.get("content")
            or last.get("text")
            or str(last)
        )


        if not answer:

    # fallback for LangGraph state objects
          for key, value in result.items():

           if isinstance(value, str) and len(value) > 20:
            answer = value
            break


        if not answer:
          answer = "Agent completed execution but no final message was generated."


        # LangGraph message format
        if not answer and result.get("messages"):

            last_message = result["messages"][-1]

            if hasattr(last_message, "content"):
                answer = last_message.content

            elif isinstance(last_message, dict):
                answer = (
                    last_message.get("content")
                    or last_message.get("text")
                )


        # fallback so frontend never gets empty
        if not answer:
            answer = (
                "I completed the engineering workflow but no final response was generated."
            )


        return {

            "answer": answer,

            "analysis": result.get(
                "analysis",
                {}
            ),

            "memory": result.get(
                "memory",
                []
            ),

            "conflict": result.get(
                "conflict_report",
                "No conflict detected"
            ),

            "execution": result.get(
                "code_changes",
                []
            )
        }


    except Exception as e:

        print("CHAT ERROR:", e)

        return {
            "error": str(e)
        }



@app.get("/chat")
def chat_info():

    return {
        "message": "Chat API is running",
        "method": "POST",
        "endpoint": "/chat"
    }