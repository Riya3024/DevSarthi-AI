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
"status": "Success",
"time": datetime.now().isoformat()
},

{
"type": "Code Analysis",
"agent": "Developer Agent",
"action": "Analyzed project structure and generated implementation plan",
"status": "Success",
"time": datetime.now().isoformat()
},


{
"type": "Documentation Update",
"agent": "Documentation Agent",
"action": "Updated engineering documentation and decision notes",
"status": "Success",
"time": datetime.now().isoformat()
}

]


@router.get("/activity")
def get_activity():

    return {
        "count": len(activities),
        "activities": activities
    }