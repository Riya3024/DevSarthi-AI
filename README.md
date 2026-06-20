# DevSarthi AI — Sentient Engineering Workspace

## Overview

DevSarthi AI is an autonomous AI engineering teammate that helps developers build, debug, review, and document software projects.

Unlike traditional coding assistants, DevSarthi AI maintains long-term project memory using **Parcle** and performs engineering workflows through a multi-agent system powered by **LangGraph** and **Enter Pro**.

The system remembers previous architectural decisions, retrieves relevant context before reasoning, executes engineering tasks, reviews changes, and updates documentation.

---

# Problem

Most AI coding assistants are stateless.

They:
- forget previous decisions
- repeat solved mistakes
- lack team context
- cannot maintain project history

DevSarthi AI solves this by creating a persistent engineering memory layer.

---

# Features

## 🧠 Persistent Engineering Memory (Parcle)

- Stores project decisions
- Saves previous fixes
- Remembers architecture choices
- Retrieves relevant context before every task

Example:

User:
Add authentication module

AI remembers:

Use Supabase Auth
Do not use Firebase
Follow existing React + FastAPI architecture

---

## 🤖 Multi-Agent Engineering System

Built with LangGraph.

Workflow:

User Request
  ↓
Project Analyzer Agent
  ↓
Memory Agent
(Parcle Retrieval)
  ↓
Developer Agent
  ↓
Enter Pro Execution Agent
  ↓
Reviewer Agent
  ↓
Documentation Agent
  ↓
Parcle Memory Update

---

# Agents

## Project Analyzer Agent

Analyzes:

- repository structure
- technology stack
- project files

## Memory Agent

Responsible for:

- retrieving previous decisions
- storing new knowledge

## Developer Agent

Acts as senior engineer.

Provides:

- implementation plans
- architecture decisions
- technical solutions

## Enter Pro Execution Agent

Uses Enter Pro workflow.

Responsibilities:

- reads project context
- prepares implementation steps
- executes engineering tasks

## Reviewer Agent

Checks:

- architecture consistency
- possible conflicts
- quality issues

## Documentation Agent

Maintains:

- README updates
- architecture notes
- project history

---

# Tech Stack

## Backend

- Python
- FastAPI
- LangGraph
- Gemini API
- Parcle Memory API

## Frontend

- React
- TypeScript
- Tailwind CSS
- Modern dashboard UI

## AI Infrastructure

- LangGraph Agent Workflow
- Parcle Persistent Memory
- Enter Pro Execution Environment

---

# Architecture

React Frontend
|
FastAPI Backend
|
LangGraph Controller
|
+----------------+----------------+----------------+

Memory Developer Reviewer Docs
| | | |
+----------------+----------------+----------------+
|
Enter Pro Executor
|
Parcle Memory Store



---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd DevSarthi-AI
```

## Backend Setup

Go to backend:
```bash
cd backend
```

Create virtual environment:
```bash
python -m venv venv
```

Activate:
- Windows:
  ```bash
  venv\Scripts\activate
  ```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create:
```bash
.env
```

Add:
```env
PARCLE_API_KEY=your_key
GEMINI_API_KEY=your_key
ENTER_PROJECT_URL=your_enter_project_url
```

## Run Backend

```bash
uvicorn main:app --reload
```

Server:
http://localhost:8000


---

# API

## Chat Endpoint

POST:
/chat


Example:
```json
{
  "message": "Add authentication module"
}
```

Response:
```json
{
  "answer": "Implementation plan...",
  "analysis": {},
  "memory": []
}
```

---

# Hackathon Track

Track:
Software — The Sentient Workspace


Built using:
- Parcle as persistent memory layer
- Enter Pro as execution environment

---

# Demo Flow

1. User gives engineering request
2. Agent searches Parcle memory
3. Developer agent reasons using context
4. Enter Pro executes workflow
5. Reviewer checks consistency
6. Documentation agent updates knowledge
7. Memory is saved for future tasks

---

# Future Improvements

- Real code patch generation
- GitHub integration
- Automated pull requests
- Team collaboration memory
- CI/CD agent

---

# Team

Built for Quackathon 2026

---

