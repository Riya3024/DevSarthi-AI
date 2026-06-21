from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


activities = [
    {
        "type": "Memory Retrieval",
        "agent": "Memory Agent",
        "action": "Retrieved Parcle memory for authentication decision",
        "status": "Success",
        "time": datetime.now().isoformat()
    },
    {
        "type": "Architecture Check",
        "agent": "Architecture Guardian Agent",
        "action": "Checked conflict with previous engineering decisions",
        "status": "Success",
        "time": datetime.now().isoformat()
    },
    {
        "type": "Code Execution",
        "agent": "Enter Pro Executor",
        "action": "Executed implementation plan in Enter environment",
        "status": "Processing",
        "time": datetime.now().isoformat()
    }
]


@router.get("/activity")
def get_activity():

    return {
        "count": len(activities),
        "activities": activities
    }