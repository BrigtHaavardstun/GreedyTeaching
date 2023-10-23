from utils.load_graph import load_witnesses, load_consitency_edge_list


def getAvgDegreeOfWitnesses(folder):
    # Make a dict over all representations. (Name -> count)
    dict_witnessSet_count = {
        rep: 0 for rep in load_witnesses(folder)}

    # Count the number of occurrences in edge list
    for (_, witness) in load_consitency_edge_list(folder):
        dict_witnessSet_count[witness] += 1

    return round(sum(dict_witnessSet_count.values()) / len(dict_witnessSet_count.keys()), 2)


if __name__ == '__main__':
    print("Average degree of witnessset:",
          getAvgDegreeOfWitnesses("boolean"))
