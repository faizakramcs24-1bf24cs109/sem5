import random

def cost(state):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def get_neighbors(state):
    neighbors = []

    for i in range(4):
        for j in range(i + 1, 4):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)

    return neighbors

def hill_climbing():
    current = random.sample(range(4), 4)

    while True:
        current_cost = cost(current)

        if current_cost == 0:
            return current

        neighbors = get_neighbors(current)
        best_neighbor = min(neighbors, key=cost)

        if cost(best_neighbor) >= current_cost:
            return current

        current = best_neighbor

solution = hill_climbing()

print("Solution:", solution)
print("Cost:", cost(solution))
