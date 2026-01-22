import bz2
import networkx as nx
from pathlib import Path

def count_graphml_bz2(path):
    with bz2.open(path, "rt") as f:
        G = nx.read_graphml(f)
    print(f"{path.name}: \nNodes = {G.number_of_nodes()} \nEdges = {G.number_of_edges()}")

if __name__ == "__main__":
    directory = Path(".")  
    for file_path in directory.glob("*3.graphml.bz2"):
        count_graphml_bz2(file_path)