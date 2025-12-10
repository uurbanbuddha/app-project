# app-project
TREDENCE


 # Minimal Workflow Engine (Assignment Submission)

## Overview
This project implements a lightweight workflow/graph engine similar to LangGraph.  
It supports:

- Nodes (Python async functions)
- Shared state propagation
- Edges and transitions
- Conditional branching
- Looping
- Tool registry
- FastAPI endpoints

Everything is in-memory for simplicity.

---

## API Endpoints

### **POST /graph/create**
Input:
```json
{
  "nodes": {"n1": "extract", "n2": "complexity", "n3": "detect", "n4": "loop"},
  "edges": {"n1": "n2", "n2": "n3", "n3": "n4"},
  "start": "n1"
}



Output:

{ "graph_id": "..." }
POST /graph/run
Input:

{
  "graph_id": "...",
  "initial_state": { "code": "def f(): pass", "threshold": 12 }
}
Output:
Final state + logs.

GET /graph/state/{run_id}
Returns current state of the run.

