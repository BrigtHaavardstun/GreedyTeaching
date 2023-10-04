from utils.load_graph import load_representations, load_consitency_edge_list


def getAvgDegreeOfConcepts(folder):
    # Make a dict over all representations. (Name -> count)
    dict_representation_count = {
        rep: 0 for rep in load_representations(folder)}

    # Count the number of occurrences in edge list
    for (rep, _) in load_consitency_edge_list(folder):
        dict_representation_count[rep] += 1

    return round(sum(dict_representation_count.values()) / len(dict_representation_count.keys()), 2)


if __name__ == '__main__':
    print("Average degree of representation:",
          getAvgDegreeOfConcepts("boolean"))
