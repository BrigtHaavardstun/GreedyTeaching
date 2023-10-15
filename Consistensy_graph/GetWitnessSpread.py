from utils.load_graph import load_representations, load_consitency_edge_list, load_witnesses
import math


def _getDictORepToNeighbourhoodRepresentations(folder):
    # concept -> [witness] (Its neighbourhood)
    dict_representation_to_neighbourhood = {rep: []
                                            for rep in load_representations(folder=folder)}  # we only care about the concept we taught

    for (representation, witness) in load_consitency_edge_list(folder):
        dict_representation_to_neighbourhood[representation].append(witness)

    return dict_representation_to_neighbourhood


def get_adjecency_graph(folder):
    adjecency_graph = {w: [] for w in load_witnesses(folder)}
    for r, w in load_consitency_edge_list(folder):
        adjecency_graph[w].append(r)
    return adjecency_graph


def getWitnessSpread(folder):
    nearnessOfRedundancy = 0

    representation_weights = {repId: int(
        repId[2:]) for repId in load_representations(folder)}

    dict_representation_to_neighbourhood = _getDictORepToNeighbourhoodRepresentations(
        folder)

    witness_spread = 0
    adjecency_graph = get_adjecency_graph(
        folder)  # Witness to representations
    for witness in load_witnesses(folder):
        dist = int(witness[2:])
        adjecency_list = adjecency_graph[witness]

        diff_concepts = set()
        for i in range(min(len(adjecency_list), dist)):
            r = adjecency_list[i]
            diff_concepts.add(
                ":".join(sorted(dict_representation_to_neighbourhood[r])))

        witness_spread += len(diff_concepts)

    return round(witness_spread/len(load_witnesses(folder)), 2)
