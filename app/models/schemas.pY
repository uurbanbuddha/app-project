from pydantic import BaseModel
from typing import Dict, Any


class GraphCreateRequest(BaseModel):
    nodes: Dict[str, str]      # node_name → function name
    edges: Dict[str, str]      # node → next node
    start: str                 # entry node


class GraphRunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]
