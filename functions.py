# functions which will be included inside of main.py

import matplotlib.pyplot as plt


def check_input(args, heights):
    if args.heights != None or args.kvals != None:
        heights_str = args.heights[0]
        user_heights = list(map(int, heights_str))
        for i in range(0, len(user_heights)):
            if user_heights[i] > heights:
                print("Input node " + str(user_heights[i]) + " does not exist.")
                exit(1)


def check_key(key, data_file):
    if key not in data_file:
        print("FILE INVALID. no {0}. Enter a valid json file.".format(key))
        exit(0)


def add_edges(data_file):
    edges =[]
    kvals = []
    numEdges = len(data_file['connections'])
    for i in range(0, numEdges):
        edges.append(data_file['connections'][i]['nodes'])
        kvals.append(data_file['connections'][i]['K'])
    return edges, kvals


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

def color_edges(G, edges, color_edges, kvals):
    color_red = []
    for i in range(0, len(edges)):
        for j in range(0, len(color_edges), 2):
            arr = []
            arr.append(color_edges[j])
            arr.append(color_edges[j+1])
            if arr[0] == edges[i][0] and arr[1] == edges[i][1]:
                color_red.append(edges[i])
                color_red.append(kvals[i])
            if arr[1] == edges[i][0] and arr[0] == edges[i][1]:
                color_red.append(edges[i])
                color_red.append(kvals[i])
            else:
                G.add_edge(edges[i][0], edges[i][1], color="black")
    return color_red


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
