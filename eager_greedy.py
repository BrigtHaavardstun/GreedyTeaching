from utils.load_graph import load_representations, load_witnesses, load_consitency_edge_list


def compatible(folder, witnessID, repsentationID):
    return [repsentationID, witnessID] in load_consitency_edge_list(folder)


def run_eager(folder):
    matching = {}
    for witnessID in load_witnesses(folder):
        print(witnessID, len(load_witnesses(folder)))
        for repsentationID in load_representations(folder):
            if compatible(folder, witnessID, repsentationID):
                if repsentationID in matching:
                    break
                else:
                    matching[repsentationID] = witnessID
                    break

    return matching


def run_greedy(folder):
    matching = {}
    for witnessID in load_witnesses(folder):
        print(witnessID, len(load_witnesses(folder)))
        for repsentationID in load_representations(folder):
            if compatible(folder, witnessID, repsentationID):
                if repsentationID in matching:
                    continue
                else:
                    matching[repsentationID] = witnessID
                    break

    return matching


def betterIdx(folder, eager, greedy):
    better = 0
    total = 0
    for repID in eager.keys():
        witnessIDEager = eager[repID]
        nrEager = int(witnessIDEager[2:])
        witnessIDGreedy = greedy[repID]
        nrGreedy = int(witnessIDGreedy[2:])

        total += 1
        if nrEager > nrGreedy:
            better += 1

    return round(better/total*100, 2)


if __name__ == '__main__':
    folder = "3-DNF_max_cardin_5"
    eager_matching = run_eager(folder)
    greedy_matching = run_greedy(folder)
    print(betterIdx(folder, eager_matching, greedy_matching))
