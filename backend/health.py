from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "checks": [
            {
                "name": "Parcle Memory",
                "status": "connected"
            },
            {
                "name": "Enter Agent",
                "status": "connected"
            },
            {
                "name": "LangGraph Workflow",
                "status": "running"
            }
        ]
    }