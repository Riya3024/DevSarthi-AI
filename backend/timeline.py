from fastapi import APIRouter
from agent.memory import ParcleMemory
from datetime import datetime

router = APIRouter()

memory = ParcleMemory()


@router.get("/timeline")
def get_timeline():

    memories = memory.search_memory(
        "project"
)

    timeline = []


    for idx, item in enumerate(memories):

        text = str(item)
        # category detection
        if "bug" in text.lower() or "fix" in text.lower():
         category = "Bug Fix"

        elif "architecture" in text.lower():
         category = "Architecture"

        elif "documentation" in text.lower() or "readme" in text.lower():
         category = "Documentation"

        else:
         category = "Decision"

        timeline.append(
    {
        "id": idx + 1,

        "type": category,

        "title":
"Engineering Decision Retrieved from Parcle",

        "decision": text[:250],

        "agent": "DevSarthi AI",

        "timestamp":
datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),

"summary": "Engineering decision retrieved from Parcle memory",


"source":
"Parcle Memory"
    }
)
        


    return {

    "project": "DevSarthi AI",

    "total_memories": len(timeline),

    "statistics": {

        "decisions": len(
            [
                x for x in timeline
                if x["type"] == "Decision"
            ]
        ),

        "architectures": len(
            [
                x for x in timeline
                if x["type"] == "Architecture"
            ]
        ),

        "total": len(timeline)
    },


    "timeline": timeline
}