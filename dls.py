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

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    depth_limit = 2
    print(f"DLS traversal starting from vertex 'A' with depth limit {depth_limit}:", dls(graph, 'A', depth_limit))