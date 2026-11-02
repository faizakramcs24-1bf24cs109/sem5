import random
import math

def cost(state):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def get_neighbor(state):
    neighbor = state.copy()

    col = random.randint(0, 7)
    row = random.randint(0, 7)

    neighbor[col] = row

    return neighbor

def simulated_annealing():
    current = [random.randint(0, 7) for _ in range(8)]
    T = 1000
    cooling_rate = 0.99

    while T > 0.1:
        next_state = get_neighbor(current)

        delta_E = cost(current) - cost(next_state)

        if delta_E > 0:
            current = next_state
        else:
            p = math.exp(delta_E / T)

            if random.random() < p:
                current = next_state

        if cost(current) == 0:
            return current

        T *= cooling_rate

    return current

solution = simulated_annealing()

print("Solution:", solution)
print("Cost:", cost(solution))

if cost(solution) == 0:
    print("Solution Found")
else:
    print("No solution found")
