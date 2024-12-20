import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time
from IPython.display import clear_output

def bfs(graph, start):
    # Initialize a set (an array with no duplicates)
    visited = set()

    # Queue for visiting the nodes
    # We start at the given start node
    queue = deque([start])

    # Initialize an empty array for the path sequence
    traversal_order = []

    # While there are still items in the queue
    while queue:
        # For each loop, we pop the queue
        # Because we need to reference the shortest path
        node = queue.popleft()

        # If the current node processed is not yet in the set
        # Meaning if we haven't processed this node yet
        if node not in visited:
            # Then of course, we add it to the set, since we've processed it now
            visited.add(node)
            # Append this to the path sequence
            traversal_order.append(node)

            # Loop thru the node's array (the neighbor)
            for neighbor in graph[node]:
                # Then their node or element
                # Also check if we've visited this
                if neighbor not in visited:
                    # Then add it to the path sequence
                    queue.append(neighbor)

    # Return the shortest path sequence
    return traversal_order

# Sample graph for BFS 
# We have no weights for this
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Set the start node as A
start_node = 'A'
# Get the traversal order returned from the bfs method
traversal_order = bfs(graph, start_node)

G = nx.Graph(graph)
pos = nx.spring_layout(G, seed=42)

def update_graph(step, delay):
    clear_output(wait=True)  

    plt.figure(figsize=(6, 6))

    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

    # We use [:step + 1] because this is the index from the start added by 1
    for node in traversal_order[:step + 1]:
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='orange', node_size=2500)

    # Initialize an empty array to store the edges (lines)
    # With their appropriate sequence
    edges_to_highlight = []
    for node in traversal_order[:step + 1]:
        for neighbor in graph[node]:
            if neighbor in traversal_order[:step + 1]:
                edges_to_highlight.append((node, neighbor))

    nx.draw_networkx_edges(G, pos, edgelist=edges_to_highlight, edge_color='orange', width=2)

    plt.title(f"BFS Traversal - Step {step + 1}")
    plt.show()
    time.sleep(delay)

for step in range(len(traversal_order)):
    update_graph(step, delay=1)

print(f"Final BFS Path Sequence: {traversal_order}")
