from utils.load_graph import load_representations, load_consitency_edge_list, load_witnesses


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


def getNearnessOfRedundancyOld(folder):
    nearnessOfRedundancy = 0

    representation_weights = {repId: int(
        repId[2:]) for repId in load_representations(folder)}
    neighbourhood_toRepresents = _getDictOfNeighboorhoodToRepresentations(
        folder)
    for (neighbourhood, representations) in neighbourhood_toRepresents.items():
        if len(representations) <= 1:
            continue  # nearnessOfRedundancy += 0
        diff_sum = 0
        pair_cunt = 0
        for i in range(len(representations)):
            rep1 = representations[i]
            for j in range(i+1, len(representations)):
                rep2 = representations[j]
                diff_sum += abs(
                    representation_weights[rep1] - representation_weights[rep2])
                pair_cunt += 1

        diff_sum /= pair_cunt
        nearnessOfRedundancy += diff_sum

    # Should we divid by number of representations
    return round(nearnessOfRedundancy/len(neighbourhood_toRepresents.keys()), 2)


def getTestSpread(folder):

    representation_weights = {repId: int(
        repId[2:]) for repId in load_representations(folder)}
    neighbourhood_toRepresents = _getDictOfNeighboorhoodToRepresentations(
        folder)

    nearnessOfRedundancy = 0

    for (neighbourhood, representations) in neighbourhood_toRepresents.items():
        n_reps = len(representations)

        min_rep = float("inf")
        min_weight = float("inf")

        for i in range(len(representations)):
            rep = representations[i]
            if representation_weights[rep] < min_rep:
                min_rep = representation_weights[rep]
                min_weight = representation_weights[rep]

        spread = 0
        for i in range(len(representations)):
            rep = representations[i]
            if min_rep == rep or min_weight == representation_weights[rep]:
                continue
            # if min_weight >= representation_weights[rep]:
            # spread += 1/(representation_weights[rep] - min_weight)
            if min_weight + len(load_witnesses(folder)) >= representation_weights[rep]:
                spread += 1

        # print(diff)

        nearnessOfRedundancy += spread

    return round(nearnessOfRedundancy/len(neighbourhood_toRepresents.keys()), 2)


def getNearnessOfRedundancy(folder):
    nearnessOfRedundancy = 0

    representation_weights = {repId: int(
        repId[2:]) for repId in load_representations(folder)}
    neighbourhood_toRepresents = _getDictOfNeighboorhoodToRepresentations(
        folder)

    nr_of_concept_non_one = 0
    for (neighbourhood, representations) in neighbourhood_toRepresents.items():
        n_reps = len(representations)

        nr_of_concept_non_one += 1
        max_rep = float("-inf")
        min_rep = float("inf")

        for i in range(len(representations)):
            rep = representations[i]
            if representation_weights[rep] > max_rep:
                max_rep = representation_weights[rep]
            if representation_weights[rep] < min_rep:
                min_rep = representation_weights[rep]

        diff = abs(max_rep - min_rep)
        # print(diff)

        nearnessOfRedundancy += diff / \
            n_reps  # Num pairs!

    # Should we divid by number of representations
    return round(nearnessOfRedundancy/len(neighbourhood_toRepresents.keys()), 2)
