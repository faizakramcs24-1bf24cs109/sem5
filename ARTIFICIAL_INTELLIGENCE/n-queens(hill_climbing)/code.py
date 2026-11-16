
import random

def calculate_heuristic(board, n):
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Check diagonal conflicts
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing(n):
    # Random initial state
    board = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        current_h = calculate_heuristic(board, n)

        if current_h == 0:
            return board

        best_board = board[:]
        best_h = current_h

        # Try moving each queen to another row
        for col in range(n):
            for row in range(n):
                new_board = board[:]
                new_board[col] = row

                h = calculate_heuristic(new_board, n)

                if h < best_h:
                    best_h = h
                    best_board = new_board

        # If no better state exists, restart
        if best_h >= current_h:
            board = [random.randint(0, n - 1)
                     for _ in range(n)]
        else:
            board = best_board


def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
n = 8

solution = hill_climbing(n)

print("Solution:")
print_board(solution, n)

print("Heuristic value:",
      calculate_heuristic(solution, n))
