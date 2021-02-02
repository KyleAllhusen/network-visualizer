import json
import sys
import networkx as nx
import matplotlib.pyplot as plt


# make sure key exists in json file.
def check_key(key):
    if key not in data_file:
        print("FILE INVALID. no {0}. Enter a valid json file.".format(key))
        exit(0)


# get file from command line arg
file = sys.argv[1]

# Initialize Graph
G = nx.Graph()

# Lists where values are stored from JSON
edges = []
heights = []
nodes = []
locations = []

with open(file, "r") as json_file:
    assert file.endswith(".json")

    data_file = json.load(json_file)

    check_key("connections")

    numEdges = len(data_file['connections'])
    for i in range(0, numEdges):
        edges.append(data_file['connections'][i]['nodes'])

    check_key("heightsByEvent")

    numHeights = len(data_file['heightsByEvent']['0'])
    if numHeights <= 0:
        print("File has no heights.")
        exit(0)

    for i in range(0, numHeights):
        idx = str(i)
        heights.append(data_file['heightsByEvent']['0'][idx])

    for name in range(0, numHeights):
        nodes.append(name)

    # Create the locations where nodes will be placed.
    x = 0
    for i in range(0, numHeights):
        tup = (x, heights[i])
        locations.append(tup)
        if x < numHeights:
            x = x + 1.0
        else:
            x = 0

# dictionary of node positions
pos = dict(zip(nodes, locations))

G.add_edges_from(edges, k=6)

fig, ax = plt.subplots()

nx.draw(G,
        pos=pos,
        ax=ax,
        with_labels=True,
        node_size=150,
        font_size=10,
        font_color="White",
        node_color="Navy")

for point in pos:
    x, y = pos[point]
    text = "[" + str(x) + "," + str(y) + "]"
    plt.text(x, y+0.25, s=text, fontsize="small", color="red",
             horizontalalignment='center')


edge_labels = nx.get_edge_attributes(G, 'k')
# nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=8, font_color='red')


limits = plt.axis('on')
ax.tick_params(left=True, labelleft=True)
ax.grid()

plt.show()
