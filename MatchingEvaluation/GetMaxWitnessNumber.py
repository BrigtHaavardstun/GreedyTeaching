from utils.load_matching import load_witness


def get_max_witness_set_nr(folder, matching):
    matching_witness = load_witness(folder, matching)
    max_witness = max(matching_witness,
                      key=lambda x: int(x[2:]))

    return max_witness
