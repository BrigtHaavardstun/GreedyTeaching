import json
import math


def get_witness_weights():
    witness_sets = json.loads(
        open("graph_info/graph-witness_sets.json", "r").read())
    witness_weights = {key: int(value[1])
                       for key, value in witness_sets.items()}
    return witness_weights


def witness_set_size(witness_id):
    return get_witness_weights()[witness_id]


def get_max_witness_set_size(filename):
    data = json.loads(open(filename, "r").read())

    # max_witness = (max(data, key=lambda x: witness_set_size(x[1])))
    max_witness = max(data, key=lambda x: int(x[1][2:]))

    return witness_set_size(max_witness[1]), max_witness[1]


def get_witness_size_data():
    originial_file = "origninal/graph-edges.json"
    greedy_file = "greedy/graph-edges.json"
    # optimal_file = "optimal/edge_list.json"
    # optimal_ten = "optimal/Optimal_teachingSize_floor_10.json"
    optimal_wi = "optimal/Optimal_teachingSize_wi.json"
    all_files = [originial_file, greedy_file, optimal_wi]
    for file in all_files:
        print(f"{file.split('/')[0]} max witness size", end=": ")
        print(get_max_witness_set_size(file))


if __name__ == "__main__":
    get_witness_size_data()
