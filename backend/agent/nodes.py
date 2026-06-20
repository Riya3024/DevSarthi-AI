from .memory import ParcleMemory

memory = ParcleMemory()





def retrieve_memory(state):

    query = state["user_query"]


    try:
        memories = memory.search_memory(query)

    except Exception:
        memories = []


    return {
        "memory": memories
    }




def save_memory(state):

    text = f"""
    Project decision:

    User request:
    {state['user_query']}

    Agent response:
    {state['response']}

    Analysis:
    {state['analysis']}
    """

    memory.save_memory(text)


    return {
        "decision": text
    }