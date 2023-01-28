graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['A'],
    'D': ['B', 'F'],
    'E': ['B', 'H', 'G'],
    'F': ['D'],
    'G': ['E', 'I', 'J'],
    'H': ['E', 'K'],
    'I': ['G', 'L'],
    'J': ['G', 'L'],
    'K': ['H'],
    'L': ['I', 'J'],
}

visited = set()  # Set to keep track of visited nodes of graph.

global c
c = 0


def dfs(visited, graph, node):  # function for dfs

    if node not in visited:
        global c
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            c += 1


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
print(c)
