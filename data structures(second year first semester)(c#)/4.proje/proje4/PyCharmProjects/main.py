import networkx as nx
import matplotlib.pyplot as plt
import networkx.exception

G1=nx.DiGraph()

list_arcs = [(0, 1, 5.0), (0, 2, 3.0), (0, 4, 2.0), (1, 2, 2.0), (1, 3, 6.0),
             (2, 1, 1.0), (2, 3, 2.0), (4, 1, 6.0), (4, 2, 10.0), (4, 3, 4.0)]

G1.add_weighted_edges_from(list_arcs)
G1.edges()

# First we import the matplotlib python plotting package
for i in range(5):
    try:
        sp = nx.dijkstra_path(G1, source=4, target=i)
        print(sp)
        G1._node[0]['pos'] = (0, 3)
        G1._node[1]['pos'] = (2, 0)
        G1._node[2]['pos'] = (1, -3)
        G1._node[3]['pos'] = (-1, -3)
        G1._node[4]['pos'] = (-2, 0)
        # The positions of each node are stored in a dictionary
        node_pos = nx.get_node_attributes(G1, 'pos')
        # The edge weights of each arcs are stored in a dictionary
        arc_weight = nx.get_edge_attributes(G1, 'weight')
        # Create a list of arcs in the shortest path using the zip command and store it in red edges
        red_edges = list(zip(sp, sp[1:]))
        # If the node is in the shortest path, set it to red, else set it to white color
        node_col = ['white' if not node in sp else 'red' for node in G1.nodes()]
        # If the edge is in the shortest path set it to red, else set it to white color
        edge_col = ['black' if not edge in red_edges else 'red' for edge in G1.edges()]
        # Draw the nodes
        nx.draw_networkx(G1, node_pos, node_color=node_col, node_size=450)
        # Draw the node labels
        # nx.draw_networkx_labels(G1, node_pos,node_color= node_col)
        # Draw the edges
        nx.draw_networkx_edges(G1, node_pos, edge_color=edge_col)
        # Draw the edge labels
        nx.draw_networkx_edge_labels(G1, node_pos, edge_labels=arc_weight)
        # Remove the axis
        plt.axis('off')
        # Show the plot
        plt.show()

    except:
        print("No path available")
G1.remove_node(1)
for j in range(4):
    try:
        sp = nx.dijkstra_path(G1, source=4, target=j)
        print(sp)
        G1._node[0]['pos'] = (0, 3)
        G1._node[2]['pos'] = (1, -3)
        G1._node[3]['pos'] = (-1, -3)
        G1._node[4]['pos'] = (-2, 0)
        # The positions of each node are stored in a dictionary
        node_pos = nx.get_node_attributes(G1, 'pos')
        # The edge weights of each arcs are stored in a dictionary
        arc_weight = nx.get_edge_attributes(G1, 'weight')
        # Create a list of arcs in the shortest path using the zip command and store it in red edges
        red_edges = list(zip(sp, sp[1:]))
        # If the node is in the shortest path, set it to red, else set it to white color
        node_col = ['white' if not node in sp else 'red' for node in G1.nodes()]
        # If the edge is in the shortest path set it to red, else set it to white color
        edge_col = ['black' if not edge in red_edges else 'red' for edge in G1.edges()]
        # Draw the nodes
        nx.draw_networkx(G1, node_pos, node_color=node_col, node_size=450)
        # Draw the node labels
        # nx.draw_networkx_labels(G1, node_pos,node_color= node_col)
        # Draw the edges
        nx.draw_networkx_edges(G1, node_pos, edge_color=edge_col)
        # Draw the edge labels
        nx.draw_networkx_edge_labels(G1, node_pos, edge_labels=arc_weight)
        # Remove the axis
        plt.axis('off')
        # Show the plot
        plt.show()
    except (networkx.exception.NetworkXNoPath):
        print("No path available")
# We then set the coordinates of each node

