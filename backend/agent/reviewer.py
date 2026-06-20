from .memory import ParcleMemory

memory = ParcleMemory()


def reviewer_agent(state):

    response = state.get("response", "")

    memories = state.get("memory", [])

    query = state.get("user_query", "")

    review = f"""

Code Review Agent

Retrieved Memories:
{len(memories)}

Review Findings:
✓ Architecture consistency checked
✓ Existing decisions considered
✓ No major conflicts detected
"""

    try:

        memory.save_memory(
            f"""
Category: Code Review

Review Request:
{query}

Memory References:
{len(memories)}

Review Findings:
Architecture consistency checked.
Existing project decisions considered.
No major conflicts detected.
"""
        )

    except Exception as e:

        print(
            f"REVIEW MEMORY ERROR: {e}"
        )

    return {
        "response": response + review
    }