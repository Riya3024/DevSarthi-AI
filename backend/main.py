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


        print("========== AGENT RESULT ==========")
        print(result)
        print("===================================")


        answer = None


        # 1. Check normal LangGraph state fields
        possible_keys = [
            "response",
            "output",
            "final_answer",
            "answer",
            "result",
            "content"
        ]


        for key in possible_keys:

            value = result.get(key)

            if value:

                answer = value
                break



        # 2. Handle LangGraph messages
        if not answer and result.get("messages"):

            messages = result["messages"]

            last_message = messages[-1]


            if hasattr(last_message, "content"):

                answer = last_message.content


            elif isinstance(last_message, dict):

                answer = (
                    last_message.get("content")
                    or last_message.get("text")
                    or last_message.get("message")
                )


            else:

                answer = str(last_message)



        # 3. Deep search fallback
        if not answer:

            for key, value in result.items():

                if isinstance(value, str) and len(value.strip()) > 20:

                    answer = value
                    print(
                        "FOUND RESPONSE FROM KEY:",
                        key
                    )
                    break



        # 4. Last fallback
        if not answer:

            answer = (
                "Agent completed execution but "
                "no final response was generated."
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


        print(
            "CHAT ERROR:",
            str(e)
        )


        return {

            "answer":
            f"Agent error: {str(e)}",

            "analysis": {},

            "memory": [],

            "conflict":
            "error",

            "execution": []
        }


       




        

    



@app.get("/chat")
def chat_info():

    return {
        "message": "Chat API is running",
        "method": "POST",
        "endpoint": "/chat"
    }