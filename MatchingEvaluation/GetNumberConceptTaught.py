from utils.load_matching import load_matching
from utils.load_graph import load_consitency_edge_list
# We want to count the number of representations with unique neighbourhoods.


def getNrOfConcepts(folder, matching):

    # Find the neighbourhood of each representation

    # concept -> [witness] (Its neighbourhood)
    dict_representation_to_neighbourhood = {rep: []
                                            for (rep, _) in load_matching(folder=folder, matching=matching)}

    for (representation, witness) in load_consitency_edge_list(folder):
        if representation in dict_representation_to_neighbourhood:  # we only care about the concept we taught
            dict_representation_to_neighbourhood[representation].append(
                witness)

    # Now find the representations with same neighbour hood in dict_representations
    neighbourhood_set = set()

    for neighbourhood in dict_representation_to_neighbourhood.values():
        neighbourhood = ":".join(sorted(neighbourhood))  # Make it hashable
        if neighbourhood not in neighbourhood_set:
            neighbourhood_set.add(neighbourhood)

    return len(neighbourhood_set)


if __name__ == "__main__":
    print(getNrOfConcepts("boolean", "greedy"))
