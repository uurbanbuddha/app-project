import ast
import time

async def extract_functions(state):
    code = state.get("code", "")

    tree = ast.parse(code)
    functions = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    state["functions"] = functions
    state["quality_score"] = 0
    return {}


async def check_complexity(state):
    funcs = state.get("functions", [])
    complexity = len(funcs) * 2
    state["complexity"] = complexity
    state["quality_score"] += max(0, 10 - complexity)
    return {}


async def detect_issues(state):
    issues = 3 if "todo" in state.get("code", "").lower() else 0
    state["issues"] = issues
    state["quality_score"] -= issues
    return {}


async def suggest_improvements(state):
    state["suggestions"] = [
        "Refactor long functions",
        "Remove TODOs",
        "Improve naming"
    ]
    return {}


async def quality_loop(state):
    threshold = state.get("threshold", 12)
    score = state.get("quality_score", 0)

    if score < threshold:
        time.sleep(1)
        state["quality_score"] += 2
        return {"next": "detect"}
    return {}


code_review_tools = {
    "extract": extract_functions,
    "complexity": check_complexity,
    "detect": detect_issues,
    "suggest": suggest_improvements,
    "loop": quality_loop
}
