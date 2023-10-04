from utils.load_matching import load_matching


def getNrOfRepresentations(folder, matching):
    return len(load_matching(folder=folder, matching=matching))
