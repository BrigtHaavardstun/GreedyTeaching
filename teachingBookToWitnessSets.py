import json


def toRepList(file, folder):
    lines = []
    with open(file, 'r') as f:
        lines = f.read().split("\n")

    representionDict = {}

    for line in lines:
        row = line.split(":")
        witnessId = row[0]
        witness = row[1]
        representionDict["w_" + witnessId] = [witness, int(witnessId)]

    with open(folder + "/graph-witness_sets.json", "w") as f:
        f.write(json.dumps(representionDict, indent=4))


if __name__ == "__main__":
    file = "SmallP3_consitensygraph_fixedRepIDWitnessID.txt"
    folder = "sudo-P3"
    toRepList(file, folder)
