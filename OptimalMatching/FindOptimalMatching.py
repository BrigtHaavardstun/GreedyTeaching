
from OptimalMatching.BipartiteMatchingNet import generate_graph, get_max_bipartite_matching, get_size_of_max_bipartite_matching
from utils.load_graph import load_consitency_edge_list, load_witnesses, load_representations

import json


def checkIfWeHaveFullMatching(witnessNr, folder):
    graph = generate_graph(
        load_consitency_edge_list(folder=folder), witness_weight=custom_witness_inclution(folder=folder), maxWintessNr=witnessNr)
    matchingSize = get_size_of_max_bipartite_matching(
        graph, representaions=load_representations(folder=folder))
    return len(load_representations(folder=folder)) == matchingSize


def getMatching(witnessNr, folder):
    graph = generate_graph(
        load_consitency_edge_list(folder), witness_weight=custom_witness_inclution(folder), maxWintessNr=witnessNr)
    matching = get_max_bipartite_matching(
        graph, representaions=load_representations(folder=folder))
    return matching


def custom_witness_inclution(folder):
    # NOTE: This assumes weight of w_i <= w_(i+1) for all i.
    original_witness_inclution = {witnessID: int(
        witnessID[2:]) for witnessID in load_witnesses(folder)}
    return original_witness_inclution


def findOptimalMatching(folder, verbose=False):
    maxWitnessNr = -1
    found = False
    max_witnessNr = int(max(load_witnesses(folder),
                        key=lambda w: custom_witness_inclution(folder)[w])[2:])
    for include_witness_up_to in range(1, max_witnessNr+1):
        if checkIfWeHaveFullMatching(witnessNr=include_witness_up_to, folder=folder):
            maxWitnessNr = include_witness_up_to
            found = True
            break

    if not found:
        raise ValueError("No full matching found")

    return getMatching(witnessNr=maxWitnessNr, folder=folder)


def findAndStoreOptimalMatching(folder):
    matching = findOptimalMatching(folder)
    edgeListMatching = [[c, matching[c]] for c in matching.keys(
    ) if c.startswith("c")]  # Keep c_1:w_1, remove w_1:c_1

    with open(f"{folder}/optimal-matching.json", "w") as f:
        f.write(json.dumps(edgeListMatching, indent=4))
