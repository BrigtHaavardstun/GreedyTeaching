
from BipartiteMatchingNet import generate_graph, max_bipartite_matching, get_concepts, get_witnesses
import numpy as np
import random
import sys
import json


def check(x, return_matching=False):
    graph = generate_graph(
        get_edge_list(), witness_weight=get_witness_weights(), concept_weight=get_concept_weights(), max_weight=x)
    result = max_bipartite_matching(graph, return_matching=return_matching)
    if return_matching:
        return result
    print(f"Results: {result}")
    concepts = get_concepts(graph)
    print(len(concepts) == result)
    return len(concepts) == result


def get_edge_list():
    edge_list = json.loads(open("graph_info/graph-edges.json", "r").read())

    return edge_list


def get_witness_weights():
    witness_sets = json.loads(
        open("graph_info/graph-witness_sets.json", "r").read())
    witness_set_weights = {key: value[1]
                           for key, value in witness_sets.items()}
    return witness_set_weights


def get_concept_weights():
    concept_sets = json.loads(
        open("graph_info/graph-concepts.json", "r").read())
    concept_weights = {key: value[1]
                       for key, value in concept_sets.items()}
    return concept_weights


if __name__ == '__main__':
    correct = -1
    found = False
    for i in range(2000):
        print(i)
        if check(i):
            correct = i
            found = True
            break
    if found:
        print(f"Answer: {i}")
    else:
        print("No answer found")

    matching_found = check(correct, True)
    nr_concepts = len(
        list(set([key for key in matching_found if key.startswith("c_")])))
    nr_witnesses = len(
        list(set([key for key in matching_found if key.startswith("w_")])))
    print(f"Unique concepts: {nr_concepts}. Unqiue witnesses: {nr_witnesses}")
    with open("Optimal_Realative_Matching.json", "w") as f:
        f.write(json.dumps(matching_found, indent=4))
