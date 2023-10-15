import json


def toRepList(file, folder):
    lines = []
    with open(file, 'r') as f:
        lines = f.read().split("\n")

    representionDict = {}

    for line in lines:
        row = line.split(":")
        conceptID = row[2].split("\t")[-1]
        concept = row[2].split("\t")[0].strip()[2:]
        representionDict["c_" + conceptID] = [concept, len(concept)]

    with open(folder + "/graph-representations.json", "w") as f:
        f.write(json.dumps(representionDict, indent=4))


if __name__ == "__main__":
    file = "SmallP3_consitensygraph_fixedRepIDWitnessID.txt"
    folder = "sudo-P3"
    toRepList(file, folder)
