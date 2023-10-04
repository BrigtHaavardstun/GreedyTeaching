import json
from utils.load_matching import load_witness


def get_witness_weights(folder):
    witness_sets = json.loads(
        open(f"{folder}/graph-witness-sets.json", "r").read())
    witness_weights = {key: int(value[1])
                       for key, value in witness_sets.items()}
    return witness_weights


def witness_set_size(folder, witness_id):
    return get_witness_weights(folder)[witness_id]


def get_max_witness_set_size(folder, matching):
    matching_witness = load_witness(folder, matching)
    max_witness = max(matching_witness,
                      key=lambda x: witness_set_size(folder, x))

    return witness_set_size(folder, max_witness)
