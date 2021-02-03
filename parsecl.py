# parser for the command line arguments

import argparse

def parsecl():
    parser = argparse.ArgumentParser(description='Get input')
    parser.add_argument('file', help="JSON file to parse data")
    parser.add_argument('-heights', help="Nodes where you wish to display the height of a given node.", action='append',
                    nargs='*')
    parser.add_argument('-kvals', help="Edges where you wish to display the k value of a given edge", nargs='*')

    args = parser.parse_args()
    return args
