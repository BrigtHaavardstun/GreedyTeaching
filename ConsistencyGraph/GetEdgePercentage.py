from utils.load_graph import load_consitency_edge_list
from utils.load_graph import load_representations
from utils.load_graph import load_witnesses


def getEdgePercentage(folder):
    # Make a dict over all representations. (Name -> count)
    nr_representations = len(load_representations(folder))
    nr_witness = len(load_witnesses(folder))

    nr_edges = len(load_consitency_edge_list(folder))

    return round(100*nr_edges / (nr_representations*nr_witness), 2)


if __name__ == '__main__':
    print("Percentage of edges in consitency graph",
          getEdgePercentage("boolean"))
