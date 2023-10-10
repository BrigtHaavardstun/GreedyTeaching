from utils.load_graph import load_representations, load_consitency_edge_list


def _getDictOfNeighboorhoodToRepresentations(folder):
    # concept -> [witness] (Its neighbourhood)
    dict_representation_to_neighbourhood = {rep: []
                                            for rep in load_representations(folder=folder)}  # we only care about the concept we taught

    for (representation, witness) in load_consitency_edge_list(folder):
        dict_representation_to_neighbourhood[representation].append(witness)

    # Now find the representations with same neighbour hood in dict_representations
    dict_neighbourhood_representations = {}

    for (representation, neighbourhood) in dict_representation_to_neighbourhood.items():
        neighbourhood = ":".join(sorted(neighbourhood))  # Make it hashable
        if neighbourhood not in dict_neighbourhood_representations:
            dict_neighbourhood_representations[neighbourhood] = [
                representation]
        else:
            dict_neighbourhood_representations[neighbourhood].append(
                representation)

    return dict_neighbourhood_representations


def getUniquenessOfRepresentations(folder):
    dict_neighbourhood_representations = _getDictOfNeighboorhoodToRepresentations(
        folder)
    uniqueness = 0
    for (neighbourhood, representations) in dict_neighbourhood_representations.items():
        uniqueness += 1/(len(representations))

    uniqueness /= len(dict_neighbourhood_representations.keys())
    return round(uniqueness, 4)
