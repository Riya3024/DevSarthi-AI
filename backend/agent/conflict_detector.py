from .llm import generate


def conflict_detector(state):

    query = state.get(
        "user_query",
        ""
    )

    memories = state.get(
        "memory",
        []
    )


    context = "\n".join(
        str(m)
        for m in memories
    )


    prompt = f"""

You are an Architecture Conflict Detector.

Your job:

Compare the new request with previous project decisions.

Previous decisions:

{context}


New request:

{query}


Check:

1. Technology conflicts
2. Architecture conflicts
3. Dependency conflicts
4. Breaking changes


Return:

If conflict exists:

CONFLICT_FOUND:
- explain old decision
- explain new request
- suggest correct approach


If no conflict:

NO_CONFLICT

"""


    result = generate(prompt)


    return {

        "conflict_report": result

    }