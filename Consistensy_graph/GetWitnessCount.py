from utils.load_graph import load_witnesses


def getNrOfWitnessSetsInConsistensyGraph(folder):
    return len(load_witnesses(folder))
