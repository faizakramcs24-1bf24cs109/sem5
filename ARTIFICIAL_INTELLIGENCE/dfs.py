def get_neighbors(state):
    """Generates valid successor states by moving the blank space (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            state_list = list(state)
            # Swap the 0 tile with the target tile
            state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))

    return neighbors


def solve_8_puzzle_dfs(start_state, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0), max_depth=20):
    """
    Solves the 8-puzzle problem using Depth-First Search with a depth limit.
    """
    # Stack stores tuples of (current_state, path_taken)
    stack = [(start_state, [start_state])]
    visited = {}

    while stack:
        current_state, path = stack.pop()

        if current_state == goal_state:
            return path

        if len(path) - 1 >= max_depth:
            continue

        if current_state in visited and visited[current_state] <= len(path):
            continue
        visited[current_state] = len(path)

        for neighbor in get_neighbors(current_state):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return None


def print_board(state):
    """Prints a 3x3 grid representation of the state."""
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print()


# --- Example Usage ---
if __name__ == "__main__":
    # Define start state (0 is the blank tile)
    # A shallow state is used because plain DFS can get lost in deep paths quickly
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    solution = solve_8_puzzle_dfs(start, goal, max_depth=15)

    if solution:
        print(f"Solution found in {len(solution) - 1} moves:\n")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("No solution found within the specified depth limit.")