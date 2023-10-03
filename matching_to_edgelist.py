import json

data = json.loads(open("Optimal_Realative_Matching.json", "r").read())

edge_list = []
for (concept, witness) in data.items():
    if "c_" in concept:
        edge_list.append([concept, witness])

with open("optimal/edge_list.json", "w") as f:
    f.write(json.dumps(edge_list, indent=4))
