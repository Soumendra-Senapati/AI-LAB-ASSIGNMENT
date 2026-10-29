from itertools import permutations

def travelling_salesman_problem(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)
    
    min_cost = float('inf')
    min_path = []
    
    # Generate all possible tours
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start
        
        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city
            
        # Return to the starting city to complete the cycle
        current_cost += graph[k][start]
        current_path.append(start)
        
        # Update minimum cost and path if found
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path
            
    return min_path, min_cost

# Main program
if _name_ == "_main_":
    n = int(input("Enter the no of cities: "))
    print("Enter the cost matrix:")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        
    start = int(input("Enter the starting city (0 to {}): ".format(n - 1)))
    
    path, cost = travelling_salesman_problem(graph, start)
    
    print("\nOptimal path:", "->".join(map(str, path)))
    print("Minimum cost:", cost)
