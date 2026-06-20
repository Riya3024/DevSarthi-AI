from .llm import generate
from .memory import ParcleMemory

from enter.executor import EnterAgent


# Initialize services
enter = EnterAgent()
memory = ParcleMemory()


def developer_agent(state):

    user_query = state.get(
        "user_query",
        ""
    )

    project_memory = state.get(
        "memory",
        []
    )

    analysis = state.get(
        "analysis",
        {}
    )


    # Prepare memory context
    if project_memory:

        memory_context = "\n".join(
            str(item)
            for item in project_memory
        )

    else:

        memory_context = (
            "No previous engineering decisions found."
        )


    #
    # Ask Enter Pro execution layer
    #
    try:

        enter_result = enter.execute(
            user_query
        )

    except Exception as e:

        enter_result = enter.execute(
    task=user_query,
    context={
        "analysis": analysis,
        "memory": memory_context
    }
)


    #
    # Agent reasoning prompt
    #
    prompt = f"""

You are DevSarthi AI,
an autonomous software engineer.

You have access to long-term project memory.

PROJECT ANALYSIS:

{analysis}


PREVIOUS ENGINEERING MEMORY:

{memory_context}


CURRENT TASK:

{user_query}


ENTER PRO EXECUTION RESULT:

{enter_result}


Your responsibilities:

1. Understand existing architecture.
2. Respect previous decisions.
3. Never introduce conflicting technologies.
4. Suggest production-ready implementation.
5. Explain what changed.
6. Create a short engineering decision summary.

Return:

Implementation:
- what should be done

Decision:
- what should be remembered for future work

"""


    response = generate(
        prompt
    )


    #
    # Extract decision memory
    #
    decision = f"""

Engineering Decision

Task:
{user_query}

Agent Output:
{response}

Execution:
{enter_result}

"""


    return {

        "response": response,

        "decision": decision,

        "code_changes": [
            enter_result
        ],

        "analysis": analysis
    }