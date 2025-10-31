def dls(graph, start, depth):
    visited = set()

    def dls_util(vertex, current_depth):
        if current_depth > depth:
            return
        visited.add(vertex)
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dls_util(neighbor, current_depth + 1)

    dls_util(start, 0)
    return visited

def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"Depth Level: {depth}")
        dls(graph, start, depth)

if __name__ == "__main__":  
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    start_node = 'A'
    max_depth = 3
    iddfs(graph, start_node, max_depth)
    