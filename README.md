# network-visualizer
Small python program to read network data from a JSON file, and generates a network graph taking into consideration graph data, specifically the height of each device.

**make sure the required dependencies are installed(requirements.txt)**

# Example Use: 

## Display heights for nodes 6 and 8, label edge 1->5 and edge 3->8 with its k-value and highlights it


**./some_path/test.json -heights 6 8 -kvals 1 5 3 8**


-heights = nodes where height should be displayed.


-kval = edges that will be labeled and highlighted -kval 1 5 3 8 will highlight [1, 5] and [3, 8]

-h or --help for help

