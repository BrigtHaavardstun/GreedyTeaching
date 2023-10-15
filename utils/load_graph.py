import json

# Cache for storing loaded data. Key: filepath, Value: parsed data.
data_cache = {}


def load_json_data(filepath):
    """
    Load and return data from a JSON file with caching.

    Parameters:
        filepath (str): The path to the JSON file.

    Returns:
        dict: The data from the JSON file.
    """
    # Check if data is already in cache.
    if filepath in data_cache:
        return data_cache[filepath]

    # If not in cache, load data, store it in cache, and return it.
    with open(filepath, "r") as file:
        data = json.load(file)
        data_cache[filepath] = data
    return data


def load_representations(folder):
    filepath = f"{folder}/graph-representations.json"
    representations = load_json_data(filepath)
    return representations.keys()


def load_consitency_edge_list(folder):
    filepath = f"{folder}/graph-edges.json"
    edge_list = load_json_data(filepath)
    return edge_list


def load_witnesses(folder):
    filepath = f"{folder}/graph-witness_sets.json"
    witness_sets = load_json_data(filepath)
    return witness_sets.keys()


def load_witness_weights(folder):
    filepath = f"{folder}/graph-witness_sets.json"
    witness_sets = load_json_data(filepath)
    return {witness_id: int(value[1]) for (witness_id, value) in witness_sets.items()}


def load_representations_weights(folder):
    filepath = f"{folder}/graph-representations.json"
    representations = load_json_data(filepath)
    return {representation_id: int(value[1]) for (representation_id, value) in representations.items()}


def load_representations_dict(folder):
    filepath = f"{folder}/graph-representations.json"
    representations_dict = load_json_data(filepath)
    return representations_dict


def load_witness_dict(folder):
    filepath = f"{folder}/graph-witness_sets.json"
    witness_sets = load_json_data(filepath)
    return witness_sets
