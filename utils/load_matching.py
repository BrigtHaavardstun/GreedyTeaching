import json


def load_matching(folder, matching):
    return json.loads(open(f"{folder}/{matching}-matching.json").read())


def load_witness(folder, matching):
    return [w for (c, w) in load_matching(folder, matching)]
