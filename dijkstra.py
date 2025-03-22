import heapq

def dijkstra(graph, start):
    # Priority queue (min-heap)
    pq = []
    heapq.heappush(pq, (0, start))  # (distance, node)
    
    # Store shortest distances, initialized to infinity
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If the popped node's distance is greater, ignore it
        if current_distance > shortest_distances[current_node]:
            continue
        
        # Process all adjacent nodes
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path is found
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return shortest_distances

# Example Graph (Adjacency List)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
}

# Run Dijkstra’s algorithm from source 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
