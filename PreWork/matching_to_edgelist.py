import json

file_name = "Optimal_teachingSize_wi.json"
data = json.loads(open(file_name, "r").read())

edge_list = []
for (concept, witness) in data.items():
    if "c_" in concept:
        edge_list.append([concept, witness])

with open("optimal/" + file_name, "w") as f:
    f.write(json.dumps(edge_list, indent=4))
