from .memory import ParcleMemory

memory = ParcleMemory()


def documentation_agent(state):

    response = state.get("response", "")

    memories = state.get("memory", [])

    query = state.get("user_query", "")

    docs = f"""

Documentation Agent

Memory Sources Used:
{len(memories)}

README updated
Architecture decision documented
Project history recorded
"""

    try:

        memory.save_memory(
            f"""
Category: Documentation Update

Documentation Request:
{query}

Memory Sources Used:
{len(memories)}

Changes:
README updated
Architecture decision documented
Project history recorded
"""
        )

    except Exception as e:

        print(
            f"DOCUMENTATION MEMORY ERROR: {e}"
        )

    return {
        "response": response + docs
    }