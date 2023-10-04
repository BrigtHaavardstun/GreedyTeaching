import json


def count_concepts_taught(file):
    data = json.loads(open(file, "r").read())
    return len(set([c for (c, w) in data]))


def start():
    originial_file = "origninal/graph-edges.json"
    greedy_file = "greedy/graph-edges.json"
    # optimal_file = "optimal/edge_list.json"
    # optimal_ten = "optimal/Optimal_teachingSize_floor_10.json"
    optimal_wi = "optimal/Optimal_teachingSize_wi.json"
    all_files = [originial_file, greedy_file, optimal_wi]
    for file in all_files:
        print(f"{file.split('/')[0]} max witness size", end=": ")
        print(count_concepts_taught(file))


if __name__ == "__main__":
    start()
