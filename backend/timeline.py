from fastapi import APIRouter
from agent.memory import ParcleMemory

router = APIRouter()

memory = ParcleMemory()


@router.get("/timeline")
def get_timeline():

    memories = memory.search_memory(
        "architecture bug fix engineering task documentation"
    )

    timeline = []

    for idx, item in enumerate(memories):

        timeline.append(
            {
                "id": idx + 1,
                "event": str(item)
            }
        )

    return {
        "count": len(timeline),
        "timeline": timeline
    }