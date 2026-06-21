from typing import TypedDict

from langgraph.graph import StateGraph, END

from .nodes import retrieve_memory, save_memory
from .project_analyzer import analyze_project
from .developer import developer_agent
from .reviewer import reviewer_agent
from .documentation import documentation_agent
from .enter_agent import enter_agent
from .conflict_detector import conflict_detector


class AgentState(TypedDict):

    user_query:str

    repo_url:str | None

    memory:list

    analysis:dict

    response:str

    decision:str

    code_changes:list

    conflict_report:str



workflow = StateGraph(AgentState)


workflow.add_node(
    "analyzer",
    analyze_project
)


workflow.add_node(
    "memory",
    retrieve_memory
)


workflow.add_node(
    "developer",
    developer_agent
)


workflow.add_node(
    "enter",
    enter_agent
)

workflow.add_node(
    "conflict",
    conflict_detector
)


workflow.add_node(
    "reviewer",
    reviewer_agent
)


workflow.add_node(
    "documentation",
    documentation_agent
)


workflow.add_node(
    "save_memory",
    save_memory
)



workflow.set_entry_point(
    "analyzer"
)



workflow.add_edge(
    "analyzer",
    "memory"
)


workflow.add_edge(
    "memory",
    "conflict"
)


workflow.add_edge(
    "conflict",
    "developer"
)


workflow.add_edge(
    "developer",
    "enter"
)


workflow.add_edge(
    "enter",
    "reviewer"
)


workflow.add_edge(
    "reviewer",
    "documentation"
)


workflow.add_edge(
    "documentation",
    "save_memory"
)


workflow.add_edge(
    "save_memory",
    END
)



agent = workflow.compile()