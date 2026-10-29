def minimax(depth, nodeIndex, ismax, scores, height):
    # Base case: target depth reached (leaf node)
    if depth == height:
        return scores[nodeIndex]
    
    if ismax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )

# Main Program
# Example leaf node values for a height 3 tree (requires 2^3 = 8 leaf nodes)
scores = [int(x) for x in input("Enter leaf node values (space-separated, e.g., 3 5 2 9 12 5 23 3): ").split()]
height = 3

result = minimax(0, 0, True, scores, height)
print("\nThe optimal value is:", result)
