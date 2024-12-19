import matplotlib.pyplot as plt
import networkx as nx
import heapq

# Define Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    
    # For visualization: Store node updates
    path_updates = {start: [start]}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

                # Track the path to each node for visualization
                path_updates[neighbor] = path_updates.get(current_node, []) + [neighbor]
    
    return distances, path_updates

# Define the graph as an adjacency list with weights
graph = {
    'A': {'B': 7, 'C': 9},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'E': 9}
}

# Run Dijkstra's algorithm
start_node = 'A'
distances, path_updates = dijkstra(graph, start_node)

# Create a NetworkX graph for visualization
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Visualization: Draw the initial graph
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')

# Draw the graph step-by-step
def update_graph(step):
    plt.clf()  # Clear the figure to redraw
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')

    # Highlight the nodes and edges for the current step
    for node in path_updates:
        if len(path_updates[node]) <= step:
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='orange', node_size=5000)
    
    # Highlight the edges along the path
    for node in path_updates:
        for i in range(1, len(path_updates[node])):
            nx.draw_networkx_edges(G, pos, edgelist=[(path_updates[node][i-1], path_updates[node][i])], edge_color='orange', width=2)

    plt.title(f"Dijkstra's Algorithm - Step {step + 1}")
    plt.pause(1)  # Pause for a moment to visualize the update

# Visualize each step
plt.figure(figsize=(8, 6))
for step in range(len(path_updates)):
    update_graph(step)

plt.show()
