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

visited = []
queue = []


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)
    global c
    c = 0
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:

            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            c=c+1



# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')  # function calling
print(c)