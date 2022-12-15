# define the graph as a dictionary where the keys are the nodes and the values are the edges
# each edge is a tuple containing the destination node and the weight of the edge
graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('C', 1), ('D', 2)],
    'C': [('B', 4), ('D', 8), ('E', 2)],
    'D': [('E', 7)],
    'E': [('D', 9)]
}

# define a function to find the shortest path between two nodes using Dijkstra's algorithm
def dijkstra(graph, start, end):
    # create a dictionary to hold the distances from the start node to each other node
    distances = {}
    
    # initialize the distances with infinite values (i.e. the distances are unknown)
    for node in graph:
        distances[node] = float('inf')
    
    # set the distance from the start node to itself to 0
    distances[start] = 0
    
    # create a dictionary to hold the previous node in the shortest path from the start node
    previous = {}
    
    # create a set to hold the nodes that have been visited
    visited = set()
    
    # create a set to hold the nodes that are still unvisited
    unvisited = set(graph.keys())
    
    # while there are still unvisited nodes
    while unvisited:
        # find the unvisited node with the smallest distance from the start node
        current = min(unvisited, key=distances.get)
        
        # if the current node is the end node, we have found the shortest path
        if current == end:
            break
        
        # mark the current node as visited
        unvisited.remove(current)
        visited.add(current)
        
        # update the distances of the neighboring nodes
        for neighbor, weight in graph[current]:
            if neighbor in visited:
                continue
            if distances[current] + weight < distances[neighbor]:
                distances[neighbor] = distances[current] + weight
                previous[neighbor] = current
    
    # create a list to hold the shortest path
    path = []
    
    # start from the end node and work backwards to the start node
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
    
    # add the start node to the beginning of the path
    path.append(start)
    
    # reverse the path to get the correct order
    path = path[::-1]
    
    return path

# test the function
print(dijkstra(graph, 'A', 'E'))  # should print ['A', 'C', 'E']
