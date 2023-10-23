from utils.load_graph import load_representations, load_consitency_edge_list
# A concept is a unique smallest representation of equviliance classes over neighborhoods.


def getNrOfConceptInConsistensyGraph(folder):
    # For each equivilance class of representation, a concept is the smallest representation in that class

    # Find the neighbourhood of each representation

    # concept -> [witness] (Its neighbourhood)
    dict_representations = {rep: [] for rep in load_representations(folder)}

    for (representation, witness) in load_consitency_edge_list(folder):
        dict_representations[representation].append(witness)

    # Now find the representations with same neighbour hood in dict_representations
    set_witness_to_representations = set()

    for witness_list in dict_representations.values():
        witness_list = ":".join(sorted(witness_list))  # Make it hashable
        if witness_list not in set_witness_to_representations:
            set_witness_to_representations.add(witness_list)

    return len(set_witness_to_representations)


if __name__ == "__main__":
    print(getNrOfConceptInConsistensyGraph("boolean"))
