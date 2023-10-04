import json


def get_witness_weights():
    witness_sets = json.loads(
        open("graph_info/graph-witness_sets.json", "r").read())
    witness_set_weights = {key: value[1]
                           for key, value in witness_sets.items()}
    return witness_set_weights


def get_concept_weights():
    concept_sets = json.loads(
        open("graph_info/graph-concepts.json", "r").read())
    concept_weights = {key: value[1]
                       for key, value in concept_sets.items()}
    return concept_weights


def get_concept_witness_pair_from_file(file_path):
    return {concept: witness for (concept, witness) in json.load(open(file_path, "r"))}


def main():

    file_original = "origninal/graph-edges.json"
    file_greedy = "greedy/graph-edges.json"
    file_optimal = "optimal/edge_list.json"

    concept_witness_original = get_concept_witness_pair_from_file(
        file_original)
    concept_witness_greedy = get_concept_witness_pair_from_file(file_greedy)
    concept_witness_optimal = get_concept_witness_pair_from_file(file_optimal)

    concept_weight_dict = get_concept_weights()
    witness_weight_dict = get_witness_weights()
    optimal_better = 0
    greedy_better = 0
    equal = 0
    for concept in concept_witness_original.keys():
        org_witness = concept_witness_original[concept]
        greedy_witness = concept_witness_greedy[concept]
        optimal_witness = concept_witness_optimal[concept]

        greedy_size = witness_weight_dict[greedy_witness]
        optimal_size = witness_weight_dict[optimal_witness]

        if greedy_size > optimal_size:
            optimal_better += 1
        elif greedy_size < optimal_size:
            greedy_better += 1
        else:
            equal += 1

        print(
            f"Concept size: {concept_weight_dict[concept]}, org: {witness_weight_dict[org_witness]}, greedy: {witness_weight_dict[greedy_witness]},  opt: {witness_weight_dict[optimal_witness]}")

    print(f"Optimal better: {optimal_better}")
    print(f"Greedy better: {greedy_better}")
    print(f"Equal better: {equal}")


if __name__ == "__main__":
    main()
