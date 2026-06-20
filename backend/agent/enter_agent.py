from enter.executor import EnterAgent


enter = EnterAgent()


def enter_agent(state):

    task = state.get(
        "user_query",
        ""
    )

    memory = state.get(
        "memory",
        []
    )

    analysis = state.get(
        "analysis",
        {}
    )


    result = enter.execute(
        task=task,
        context={
            "memory": memory,
            "analysis": analysis
        }
    )


    return {
        "code_changes": [
            result
        ]
    }