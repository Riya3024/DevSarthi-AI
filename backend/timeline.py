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

        timeline.append(
    {
        "id": idx + 1,

        "type":
        "Architecture" if "architecture" in text.lower()
        else "Decision",

        "title":
"Engineering Decision Retrieved from Parcle",

        "decision": text,

        "agent": "DevSarthi AI",

        "timestamp":
datetime.utcnow().isoformat(),


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