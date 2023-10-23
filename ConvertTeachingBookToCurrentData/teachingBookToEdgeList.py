import json


def TeachingBookToEdgeList(folder, file, new_file):
    lines = []
    with open(file, 'r') as f:
        lines = f.read().split("\n")

    edgeList = []

    for line in lines:
        row = line.split(":")
        witnessId = row[0]
        conceptID = row[2].split("\t")[-1]

        edgeList.append(["c_" + conceptID, "w_" + witnessId])

    with open(f"{folder}/{new_file}.json", 'w') as f:
        f.write(json.dumps(edgeList, indent=4))


if __name__ == '__main__':
    folder = "Data/small-P3"
    new_file = "graph-edges"
    read_from = "SmallP3_consitensygraph_fixedRepIDWitnessID.txt"
    TeachingBookToEdgeList(folder, read_from, new_file)
