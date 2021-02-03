import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from parsecl import *
from functions import *

# parse command line
args = parsecl()

# get file from command line arg
file = args.file

# Initialize Graph
G = nx.Graph()

# Lists where values are stored from JSON
nodes = []

with open(file, "r") as json_file:

    assert file.endswith(".json")
    data_file = json.load(json_file)

    check_key("connections", data_file)
    edges = add_edges(data_file)

    check_key("heightsByEvent", data_file)
    heights = add_heights(data_file)

    # assuming nodes are named 1, 2, 3 . . . name each node
    numHeights = len(data_file['heightsByEvent']['0'])
    for name in range(0, numHeights):
        nodes.append(name)

    # Create the locations where nodes will be placed.
    locations = make_coordinates(data_file, heights)

json_file.close()

label_edges_str = args.kvals
label_edges = list(map(int, label_edges_str))
color_red = []
for i in range(0, len(edges)):
    for j in range(0, len(label_edges), 2):
        arr = []
        arr.append(label_edges[j])
        arr.append(label_edges[j+1])
        if arr[0] == edges[i][0] and arr[1] == edges[i][1]:
            color_red.append(edges[i])
        else:
            G.add_edge(edges[i][0], edges[i][1], color="black")

for i in range(0, len(color_red)):
    G.add_edge(color_red[i][0], color_red[i][1], color="red")

colors = nx.get_edge_attributes(G, 'color').values()
weights = nx.get_edge_attributes(G, 'weight').values()

# G.add_edges_from(edges)

label_heights_str = args.heights[0]
label_heights = list(map(int, label_heights_str))

color_map = make_node_color_map(G, label_heights)

# dictionary of node positions
pos = dict(zip(nodes, locations))
fig, ax = plt.subplots()

nx.draw(G,
        pos=pos,
        ax=ax,
        with_labels=True,
        node_size=150,
        font_size=10,
        edge_color=colors,
        font_color="White",
        node_color=color_map)

labelH(pos, label_heights)

edge_labels = nx.get_edge_attributes(G, 'k')
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=8, font_color='red')


limits = plt.axis('on')
ax.tick_params(left=True, labelleft=True)
ax.grid()

plt.show()
