import matplotlib.pyplot as plt


def check_key(key, data_file):
    if key not in data_file:
        print("FILE INVALID. no {0}. Enter a valid json file.".format(key))
        exit(0)

def add_edges(data_file):
    edges =[]
    numEdges = len(data_file['connections'])
    for i in range(0, numEdges):
        edges.append(data_file['connections'][i]['nodes'])
    return edges

def add_heights(data_file):
    heights = []
    numHeights = len(data_file['heightsByEvent']['0'])
    for i in range(0, numHeights):
        idx = str(i)
        heights.append(data_file['heightsByEvent']['0'][idx])
    return heights


def make_coordinates(file, heights):
    locations = []
    numHeights = len(file['heightsByEvent']['0'])
    x = 0
    for i in range(0, numHeights):
        tup = (x, heights[i])
        locations.append(tup)
        if x < numHeights:
            x = x + 1.0
        else:
            x = 0
    return locations


def make_node_color_map(G, array):
    color_map = []
    for node in G:
        if node in array:
            color_map.append('red')
        else:
            color_map.append('Navy')
    return color_map


def labelH(pos, heights):
    num = 0
    for point in pos:
        if num in heights:
            x, y = pos[point]
            text = str(y)
            plt.text(x, y + 0.25, s=text, fontsize="medium", color="red",
                     horizontalalignment='center')
        num += 1
