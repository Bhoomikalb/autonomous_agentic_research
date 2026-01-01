def supervisor(state):
    state["iterations"] = state.get("iterations", 0) + 1
    return state
