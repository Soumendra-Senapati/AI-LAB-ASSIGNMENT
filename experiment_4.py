graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        # Find the node in open_list with the lowest f(n) = g(n) + h(n)
        current_node_with_cost = min(open_list, key=lambda n: n[1] + heuristic[n[0]])
        open_list.remove(current_node_with_cost)
        current_node = current_node_with_cost[0]
        
        if current_node == goal:
            path = [goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_cost[goal]
        
        for neighbor, cost in graph[current_node]:
            new_cost = g_cost[current_node] + cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                open_list.append((neighbor, new_cost))
                
    return None, float('inf')

# Main Program
start = input("Enter the start node: ")
goal = input("Enter the Goal Node: ")

path, cost = astar(start, goal)

if path:
    print("Path found:", path)
    print("Total cost:", cost)
else:
    print("Path not found")
