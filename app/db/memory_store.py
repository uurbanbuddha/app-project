import uuid

GRAPH_STORE = {}
RUN_STORE = {}

def gen_id():
    return str(uuid.uuid4())
