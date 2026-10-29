# Function to perform DFS
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(graph, neighbour, visited)

# Main Program
graph = {}
n = int(input("Enter the no. of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    # Input adjacent vertices separated by spaces (e.g., B C)
    neighbours = input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex] = neighbours

start = input("Enter the starting vertex: ")
print("\nGraph:", graph)
print("DFS Traversal: ", end="")

visited = set()
dfs(graph, start, visited)
