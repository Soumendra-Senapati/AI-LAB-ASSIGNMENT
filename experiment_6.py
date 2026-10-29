import math

def alphabeta(depth, node_index, maximizing_player, values, alpha, beta, height):
    # Terminal condition (reached maximum depth)
    if depth == height:
        return values[node_index]
    
    if maximizing_player:
        best = -math.inf
        for i in range(2):
            value = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Main Program
# Enter 8 leaf node values for height = 3 (e.g., 3 5 6 9 1 2 0 -1)
values = list(map(int, input("Enter the 8 leaf node values (space-separated): ").split()))
height = 3

result = alphabeta(0, 0, True, values, -math.inf, math.inf, height)
print("The optimal value:", result)
