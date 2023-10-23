from utils.load_graph import load_representations


def getNrOfRepresentationsInConsistensyGraph(folder):
    return len(load_representations(folder))
