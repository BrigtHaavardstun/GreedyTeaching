from utils.load_graph import load_representations, load_consitency_edge_list, load_witnesses
from OptimalMatching.BipartiteMatchingNet import generate_graph, get_max_bipartite_matching

import json


def getMinRepresentationOfConcept(folder):
    # For each equivilance class of representation, a concept is the smallest representation in that class

    # Find the neighbourhood of each representation

    # concept -> [witness] (Its neighbourhood)
    dict_representations = {rep: [] for rep in load_representations(folder)}

    for (representation, witness) in load_consitency_edge_list(folder):
        dict_representations[representation].append(witness)

    dict_rep_weight = {rep: int(rep[2:])
                       for rep in load_representations(folder)}

    # Now find the representations with same neighbour hood in dict_representations
    dict_neighbourhood_to_minRep = {}

    for (rep, witness_list) in dict_representations.items():
        witness_list = ":".join(sorted(witness_list))  # Make it hashable
        if witness_list not in dict_neighbourhood_to_minRep:
            dict_neighbourhood_to_minRep[witness_list] = rep
        elif dict_rep_weight[dict_neighbourhood_to_minRep[witness_list]] > dict_rep_weight[rep]:
            dict_neighbourhood_to_minRep[witness_list] = rep

    return sorted(dict_neighbourhood_to_minRep.values(), key=lambda x: dict_rep_weight[x])


def custom_witness_inclution(folder):
    # NOTE: This assumes weight of w_i <= w_(i+1) for all i.
    original_witness_inclution = {witnessID: int(
        witnessID[2:]) for witnessID in load_witnesses(folder)}
    return original_witness_inclution


def getGraphOnRepPerConcept(folder):
    repList = getMinRepresentationOfConcept(folder)
    edge_list = [(c, w)
                 for (c, w) in load_consitency_edge_list(folder) if c in repList]
    witness_weights = custom_witness_inclution(folder)
    conceptGraph = generate_graph(
        edge_list=edge_list, witness_weight=witness_weights)
    conceptMatching = get_max_bipartite_matching(
        graph=conceptGraph, representaions=repList)

    size = len(conceptMatching)//2
    # print(size)
    return conceptMatching


def getOptimalMatchingConceptAndRest(folder):
    conceptMatching = getGraphOnRepPerConcept(folder)
    representaionsInConceptMatching = [
        c for (c, w) in conceptMatching.items() if c.startswith("c_")]
    witnessInConceptMatching = [
        w for (c, w) in conceptMatching.items() if w.startswith("w_")]
    restRepresentations = list(filter(lambda x: x not in representaionsInConceptMatching, load_representations(
        folder)))
    restWitness = [w for w in load_witnesses(
        folder) if w not in witnessInConceptMatching]

    # E*256 was to slow, improves to E*(1) instead
    used_rep_in_con = [
        True]*(int(max(load_representations(folder), key=lambda r: int(r[2:]))[2:])+1)
    for rep in representaionsInConceptMatching:
        used_rep_in_con[int(rep[2:])] = False

    used_wit_in_con = [
        True]*(int(max(load_witnesses(folder), key=lambda w: int(w[2:]))[2:])+1)
    for wit in witnessInConceptMatching:
        used_wit_in_con[int(wit[2:])] = False

    restEdgeList = []
    for (c, w) in load_consitency_edge_list(folder):
        if used_rep_in_con[int(c[2:])] and used_wit_in_con[int(w[2:])]:
            restEdgeList.append([c, w])
    witness_weights = custom_witness_inclution(folder)
    restGraph = generate_graph(
        edge_list=restEdgeList, witness_weight=witness_weights)

    # Remove representations that does not have an edge in the remaining graph
    restRepresentations_removed = []
    for c in restRepresentations:
        if c in [c for (c, w) in restEdgeList]:
            restRepresentations_removed.append(c)
    restMaxMatching = get_max_bipartite_matching(
        graph=restGraph, representaions=restRepresentations_removed)

    # print(len(restMaxMatching)//2)
    # print("Total size:", len(restMaxMatching)//2+len(conceptMatching)//2)

    combinedMatching = {}
    for (key, value) in restMaxMatching.items():
        combinedMatching[key] = value

    for (key, value) in conceptMatching.items():
        combinedMatching[key] = value

    return combinedMatching


def findAndStoreNewOptimalMatching(folder):
    matching = getOptimalMatchingConceptAndRest(folder)
    edgeListMatching = [[c, matching[c]] for c in matching.keys(
    ) if c.startswith("c")]  # Keep c_1:w_1, remove w_1:c_1

    with open(f"{folder}/optimalNew-matching.json", "w") as f:
        f.write(json.dumps(edgeListMatching, indent=4))
