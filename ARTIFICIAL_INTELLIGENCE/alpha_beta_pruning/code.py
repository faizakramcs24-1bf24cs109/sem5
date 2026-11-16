import math

def alpha_beta(depth, node_index, is_maximizing, values, alpha, beta, max_depth):
    # Base case: reached a leaf node (end of the game tree)
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        best = -math.inf

        # Recur for left and right children (branching factor = 2)
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning condition
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        # Recur for left and right children
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning condition
            if beta <= alpha:
                break

        return best

# --- Example Usage ---
# Leaf node scores for a binary tree of depth 3 (2^3 = 8 leaf nodes)
leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
tree_depth = 3

optimal_value = alpha_beta(
    depth=0,
    node_index=0,
    is_maximizing=True,
    values=leaf_values,
    alpha=-math.inf,
    beta=math.inf,
    max_depth=tree_depth
)

print("Optimal value:", optimal_value)  # Output: 5
