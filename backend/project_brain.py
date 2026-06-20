from fastapi import APIRouter
from agent.memory import ParcleMemory
from agent.llm import generate

router = APIRouter()

memory = ParcleMemory()


@router.get("/project-brain")
def project_brain(q: str):

    try:
        memories = memory.search_memory(q)

        if not memories:
            memories = []

        context = "\n".join(
            str(m) for m in memories
        )

        prompt = f"""
You are DevSarthi AI.

You are a senior engineering teammate with long-term memory.

PROJECT MEMORY:
{context}

QUESTION:
{q}

Instructions:
- Use project memory first.
- Reference previous architectural decisions.
- Reference previous bug fixes.
- Reference documentation knowledge.
- If memory is empty, clearly state that no relevant project memory was found.
"""

        answer = generate(prompt)

        return {
            "success": True,
            "question": q,
            "memory_count": len(memories),
            "answer": answer
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
    
@router.get("/brain-summary")
def brain_summary():

    memories = memory.search_memory(
        "architecture decisions bug fixes project history documentation"
    )

    return {
        "memories": memories
    }

@router.get("/knowledge")
def knowledge_base():

    memories = memory.search_memory(
        "architecture decisions bug fixes documentation"
    )

    return {
        "knowledge": memories
    }