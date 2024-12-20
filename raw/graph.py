from IPython.display import clear_output
import matplotlib.pyplot as plt
import networkx as nx
import heapq
import time

def dijkstra(graph, start):
    # Initialize distances as infinity for each node in the graph 
    distances = {node: float('inf') for node in graph}
    # Set the start node as 0 
    distances[start] = 0
    # Initialize priority queue as key-value pair tuple
    # This would show up as (0,0) initially
    priority_queue = [(0, start)]  
    
    # Initiate an object with the key as start
    # Updating its value with the start node
    # This is the sequence of the path
    path_updates = {start: [start]}
    
    # Traverse while there are still items in the priority queue
    # From the process here, the priority queue will have been modified with new tuples
    while priority_queue:
        # Pop the smallest (distance, node) pair from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip everything if the current distance is greater than the known shortest distance
        if current_distance > distances[current_node]:
            continue
        
        # Loop thru the graph's items of the smallest known node
        # Check the surrounding neighbours (their object keys)
        # Check the surrounding weights (their object values)
        for neighbor, weight in graph[current_node].items():
            # Reference their distance by adding the shortest known distance and the current item's weight
            distance = current_distance + weight

            # If the distance calculated is less than the next column's (object key) distance (object value)
            if distance < distances[neighbor]:
                # Then set this as the new shortest known distance
                distances[neighbor] = distance
                # Push the tuple (distance, node) to the priority queue
                # So that we can reference it next
                heapq.heappush(priority_queue, (distance, neighbor))

                # Add a new key to the path updates
                # Their value will be the key of the shortest path
                # If the current node has no path yet, we initialize an empty array for it
                # Then add it's neighbor's value
                path_updates[neighbor] = path_updates.get(current_node, []) + [neighbor]
    
    # Return the shortest distances and the paths to each node from the start
    return distances, path_updates

# Our sample graph
graph = {
    'A': {'B': 7, 'C': 9},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'E': 9}
}

# We start at this node (row 0)
start_node = 'A'
# Get the distances and path sequence from the method
distances, path_updates = dijkstra(graph, start_node)

# Initialize a graph
G = nx.Graph()

# Traverse thru the graph's items
for node, neighbors in graph.items():
    # Get the their objects
    for neighbor, weight in neighbors.items():
        # For each key and value of their object
        # We add the edge, their parent key, the key we're traversing thru and their associated weight
        G.add_edge(node, neighbor, weight=weight)

# Initialize a spring layout
pos = nx.spring_layout(G, seed=42)  

# Helper method
def update_graph(step, delay):
    # For each update, we clear the layout
    # Wait is set to true so the process won't go on
    clear_output(wait=True) 
    
    # Set the size of output
    plt.figure(figsize=(6, 6))

    # We draw the nodes with their configurations
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')
    
    # Loop thru nodes in the path sequence
    for node in path_updates:
        # To avoid exceeding the number of nodes in the path updates
        if len(path_updates[node]) <= step:
            # Then draw the current node being processed with their configuration
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='orange', node_size=2500)
    
    for node in path_updates:
        # Loop thru the path updates with the current node being processed
        # Start at 1 then end with the length of the values
        for i in range(1, len(path_updates[node])):
            # Draw the lines that connect to the next node
            nx.draw_networkx_edges(G, pos, edgelist=[(path_updates[node][i-1], path_updates[node][i])], edge_color='orange', width=2)

    plt.title(f"Dijkstra's Algorithm - Step {step + 1}")
    plt.show()
    time.sleep(delay)  

# For each step, we delay updating the graph by 1 second
for step in range(len(path_updates)):
    update_graph(step, delay=1)  
