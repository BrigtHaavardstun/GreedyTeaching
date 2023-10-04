import json


def load_representations(folder):
    representations = json.loads(
        open(f"{folder}/graph-representations.json").read())
    return representations.keys()


def load_consitency_edge_list(folder):
    edge_list = json.loads(open(f"{folder}/graph-edges.json").read())
    return edge_list


def load_witnesses(folder):
    witnesssets = json.loads(
        open(f"{folder}/graph-witness-sets.json").read())
    return witnesssets.keys()