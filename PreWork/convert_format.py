from can_we_find_a_full_matching import get_witness_weights, get_concept_weights
import json


def get_witness_witnessID():
    witness_sets = json.loads(
        open("graph_info/graph-witness_sets.json", "r").read())
    witness_set_weights = {str(value[0]): key
                           for key, value in witness_sets.items()}
    return witness_set_weights


def get_concept_conceptID():
    concept_sets = json.loads(
        open("graph_info/graph-concepts.json", "r").read())
    concept_weights = {str(value[0]).replace("V", "or"): key
                       for key, value in concept_sets.items()}
    return concept_weights


# we do not have the concept/witness IDs and concept/witness sizes. To get this we need to load the concept file,
# to ensure we have a consitant mapping
dict_concept_conceptId = get_concept_conceptID()
dict_witness_witnessId = get_witness_witnessID()


# Sample input data
files = ["greedy/(c-ii)-results-n_3-Greedy.txt",
         "origninal/(c-i)-results-n_3-Orig.txt"]


for file in files:
    data = ""
    with open(file, "r") as f:
        data = f.read()
    # Splitting the data into lines
    lines = data.split("\n")

    # Extracting the relevant information

    matching = {}
    for line in lines[2:]:  # Ignoring the first two lines
        parts = line.split(":")
        # In weighted we have [["000","1"]], in report we hvae [("000","1")]
        w = parts[1].strip().replace('(', '[').replace(')', ']')
        concept = parts[2].strip()
        if concept == "None":
            continue
        elif dict_concept_conceptId[concept] in matching:
            continue
        matching[dict_concept_conceptId[concept]] = dict_witness_witnessId[w]

    edge_list = []
    for (concept, witness) in matching.items():
        edge_list.append([concept, witness])

    folder = file.split("/")[0]
    with open(folder + "/graph-edges.json", "w") as f:
        f.write(json.dumps(edge_list, indent=4))
