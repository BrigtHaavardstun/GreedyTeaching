from utils.load_matching import load_witness
from utils.load_graph import load_witness_weights


def witness_set_size(folder, witness_id):
    return load_witness_weights(folder)[witness_id]


def get_max_witness_set_size(folder, matching):
    matching_witness = load_witness(folder, matching)
    max_witness = max(matching_witness,
                      key=lambda x: witness_set_size(folder, x))

    return witness_set_size(folder, max_witness)
