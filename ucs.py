import heapq

def uniform_cost_search(start, goal_test, get_neighbors, get_cost):
    
    frontier = []
    heapq.heappush(frontier, (0, start, []))

    explored = set()

    while frontier:

        cost, state, path = heapq.heappop(frontier)

        if goal_test(state):
            return cost, path

        if state in explored:
            continue

        explored.add(state)

        for neighbor, action in get_neighbors(state):
            if neighbor not in explored:
                total_cost = cost + get_cost(state, neighbor)
                heapq.heappush(frontier, (total_cost, neighbor, path + [action]))

    return None 

if __name__ == "__main__":
    
    graph = {
        'A': [('B', 'go to B'), ('C', 'go to C')],
        'B': [('D', 'go to D'), ('E', 'go to E')],
        'C': [('F', 'go to F')],
        'D': [],
        'E': [('F', 'go to F')],
        'F': []
    }

    costs = {
        ('A', 'B'): 1,
        ('A', 'C'): 4,
        ('B', 'D'): 2,
        ('B', 'E'): 5,
        ('C', 'F'): 1,
        ('E', 'F'): 2
    }

    def goal_test(state):
        return state == 'F'

    def get_neighbors(state):
        return graph.get(state, [])

    def get_cost(from_state, to_state):
        return costs.get((from_state, to_state), float('inf'))

    result = uniform_cost_search('A', goal_test, get_neighbors, get_cost)
    if result:
        total_cost, path = result
        print(f"Total cost: {total_cost}, Path: {path}")
    else:
        print("No path found.")
    