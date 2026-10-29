from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0, [])])  # (jug1, jug2, path)
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))
        current_path = path + [(jug1, jug2)]
        
        # Check if target is reached
        if jug1 == target or jug2 == target:
            return current_path
        
        # Generate all possible next states
        next_states = [
            (capacity1, jug2),                      # Fill Jug 1
            (jug1, capacity2),                      # Fill Jug 2
            (0, jug2),                              # Empty Jug 1
            (jug1, 0),                              # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),
            # Pour Jug 2 -> Jug 1
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], current_path))
                
    return None

# Main Program
capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug(capacity1, capacity2, target)

if solution:
    print("\nSteps to reach the target:")
    for step in solution:
        print(step)
else:
    print("No solution exist")
