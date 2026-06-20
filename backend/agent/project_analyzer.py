def analyze_project(state):

    repo_url = state.get("repo_url")


    analysis = {
        "repository": repo_url,
        "stack": [
            "React",
            "FastAPI",
            "PostgreSQL"
        ],
        "files": [
            "frontend/src",
            "backend/main.py",
            "requirements.txt"
        ]
    }


    state["analysis"] = analysis


    return {
        "analysis": analysis
    }