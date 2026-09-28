def get_neighbors(state):
    """Generates valid successor states by moving the blank space (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            state_list = list(state)
            state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))

    return neighbors


def depth_limited_search(state, goal_state, limit, path, visited_at_depth):
    """Recursive Depth-Limited Search helper function."""
    if state == goal_state:
        return path

    if limit <= 0:
        return None

    # Track depth to avoid revisiting nodes deeper than necessary
    current_depth = len(path)
    if state in visited_at_depth and visited_at_depth[state] <= current_depth:
        return None
    visited_at_depth[state] = current_depth

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(
                neighbor, 
                goal_state, 
                limit - 1, 
                path + [neighbor], 
                visited_at_depth
            )
            if result is not None:
                return result

    return None


def solve_8_puzzle_ids(start_state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0), max_limit=30):
    """
    Solves the 8-puzzle using Iterative Deepening Search (IDS/IDDFS).
    """
    for depth in range(max_limit + 1):
        visited_at_depth = {}
        result = depth_limited_search(start_state, goal_state, depth, [start_state], visited_at_depth)
        if result is not None:
            return result, depth

    return None, None


def print_board(state):
    """Prints a 3x3 grid representation of the state."""
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print()


if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    solution, total_depth = solve_8_puzzle_ids(start, goal)

    if solution:
        print(f"Optimal solution found at depth {total_depth} ({len(solution) - 1} moves):\n")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("No solution found within the maximum depth limit.")