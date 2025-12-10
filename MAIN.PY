from fastapi import FastAPI, HTTPException
from app.models.schemas import GraphCreateRequest, GraphRunRequest
from app.db.memory_store import GRAPH_STORE, RUN_STORE
from app.engine.graph_engine import GraphEngine

app = FastAPI(title="Workflow Engine")

engine = GraphEngine()


@app.post("/graph/create")
async def create_graph(request: GraphCreateRequest):
    graph_id = engine.create_graph(
        nodes=request.nodes,
        edges=request.edges,
        start=request.start
    )
    return {"graph_id": graph_id}


@app.post("/graph/run")
async def run_graph(request: GraphRunRequest):
    if request.graph_id not in GRAPH_STORE:
        raise HTTPException(status_code=404, detail="Graph not found")

    run_id, final_state, logs = await engine.run_graph(
        graph_id=request.graph_id, 
        initial_state=request.initial_state
    )
    return {
        "run_id": run_id,
        "final_state": final_state,
        "logs": logs
    }


@app.get("/graph/state/{run_id}")
async def get_state(run_id: str):
    if run_id not in RUN_STORE:
        raise HTTPException(status_code=404, detail="Run not found")
    return {"state": RUN_STORE[run_id]["state"]}
