from app.db.memory_store import GRAPH_STORE, gen_id
from app.engine.runner import Runner
from app.workflows.code_review_agent import code_review_tools


class GraphEngine:

    def create_graph(self, nodes, edges, start):
        graph_id = gen_id()

        fn_map = {}
        for node, tool_name in nodes.items():
            fn_map[node] = code_review_tools[tool_name]

        GRAPH_STORE[graph_id] = {
            "nodes": fn_map,
            "edges": edges,
            "start": start
        }
        return graph_id

    async def run_graph(self, graph_id, initial_state):
        graph = GRAPH_STORE[graph_id]
        runner = Runner()
        logs = []
        return await runner.run(
            graph=graph, 
            start_node=graph["start"], 
            initial_state=initial_state, 
            logs=logs
        )
