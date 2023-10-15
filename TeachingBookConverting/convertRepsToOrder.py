
from utils.load_graph import load_representations, load_representations_dict, load_consitency_edge_list
import json


def fixRepresentation(folder, dict_old_id_to_new_id):
    old_representations = load_representations_dict(folder)
    new_dict = {}

    for (repID, info) in old_representations.items():
        new_id = dict_old_id_to_new_id[repID]
        new_dict[new_id] = info

    with open(folder + "/graph-representations.json", "w") as f:
        f.write(json.dumps(new_dict, indent=4))


def fixEdgeList(folder, dict_old_id_to_new_id):
    old_edge_list = load_consitency_edge_list(folder)
    new_edge_list = []
    for (conceptID, witnessID) in old_edge_list:
        newConceptID = dict_old_id_to_new_id[conceptID]
        new_edge_list.append([newConceptID, witnessID])

    with open(folder + "/graph-edges.json", "w") as f:
        f.write(json.dumps(new_edge_list, indent=4))


def convertRepsToBeIdInOrder(folder):
    currentReps = sorted(load_representations(
        folder), key=lambda x: int(x[2:]))

    dict_old_id_to_new_id = {}

    for (i, curreRep) in enumerate(currentReps):
        i = i + 1  # want to start at 1
        dict_old_id_to_new_id[curreRep] = "c_" + str(i)

    fixRepresentation(folder, dict_old_id_to_new_id)
    fixEdgeList(folder, dict_old_id_to_new_id)


if __name__ == "__main__":
    folder = "sudo-P3"
    convertRepsToBeIdInOrder(folder)
