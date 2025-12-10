import asyncio
from app.engine.state import State
from app.db.memory_store import RUN_STORE, gen_id


class Runner:

    async def run(self, graph, start_node, initial_state, logs):
        state = State(initial_state)
        run_id = gen_id()

        RUN_STORE[run_id] = {"state": state}

        current = start_node

        while current:
            fn = graph["nodes"][current]

            logs.append(f"Running node: {current}")
            result = await fn(state)

            RUN_STORE[run_id]["state"] = state

            # handle loop
            if isinstance(result, dict) and "next" in result:
                current = result["next"]
            else:
                current = graph["edges"].get(current)

        return run_id, state, logs
