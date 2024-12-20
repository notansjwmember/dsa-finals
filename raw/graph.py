from IPython.display import clear_output
import matplotlib.pyplot as plt
import networkx as nx
import heapq
import time

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  
    
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

                
                path_updates[neighbor] = path_updates.get(current_node, []) + [neighbor]
    
    return distances, path_updates

graph = {
    'A': {'B': 7, 'C': 9},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'E': 9}
}

start_node = 'A'
distances, path_updates = dijkstra(graph, start_node)

G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, seed=42)  

def update_graph(step, delay=1):
    clear_output(wait=True)  
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')
    
    for node in path_updates:
        if len(path_updates[node]) <= step:
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='orange', node_size=2500)
    
    for node in path_updates:
        for i in range(1, len(path_updates[node])):
            nx.draw_networkx_edges(G, pos, edgelist=[(path_updates[node][i-1], path_updates[node][i])], edge_color='orange', width=2)

    plt.title(f"Dijkstra's Algorithm - Step {step + 1}")
    plt.show()
    time.sleep(delay)  

for step in range(len(path_updates)):
    update_graph(step, delay=1)  
