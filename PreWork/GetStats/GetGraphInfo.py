import json


def load_consitency_edge_list():
    edge_list = json.loads(open("graph_info/graph-edges.json").read())
    return edge_list


def get_concepts():
    # For each equivilance class of representation, a concept is the smallest representation in that class
    dict_representations = {}  # concept -> [witness]
    for (representation, witness) in load_consitency_edge_list():
        if representation not in dict_representations:
            dict_representations[representation] = []

        dict_representations[representation].append(witness)

    # Now find the simillar representations in dict_representations

    dict_witness_to_representations = {}

    for (representation, witness_list) in dict_representations.items():
        witness_list = ":".join(sorted(witness_list))
        if witness_list not in dict_witness_to_representations:
            dict_witness_to_representations[witness_list] = representation
        elif dict_witness_to_representations[witness_list] > representation:
            dict_witness_to_representations[witness_list] = representation

    # for w in dict_witness_to_representations:
    #    print(w, dict_witness_to_representations[w])

    return (len(dict_witness_to_representations))


if __name__ == "__main__":
    print(get_concepts())
