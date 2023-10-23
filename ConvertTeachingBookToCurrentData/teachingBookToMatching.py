
from utils.load_graph import load_representations_dict
import json


def getConceptID(folder, concept):
    return [c for (c, values) in load_representations_dict(folder).items() if concept == values[0]][0]


def TeachingBookToMatching(folder, file, new_file):
    lines = []
    with open(file, 'r') as f:
        lines = f.read().split("\n")

    edgeList = []

    for line in lines:
        row = line.split(":")
        witnessId = row[0]
        concept = row[2].split("\t")[0].strip()[2:]

        conceptID = getConceptID(folder, concept)
        edgeList.append([conceptID, "w_" + witnessId])

    with open(f"{folder}/{new_file}.json", 'w') as f:
        f.write(json.dumps(edgeList, indent=4))


if __name__ == '__main__':
    folder = "Data/small-P3"
    read_from_file = "small_P3-Greedy-k_4-TB.txt"
    new_file = "greedy-matching"
    TeachingBookToMatching(folder, read_from_file, new_file)
