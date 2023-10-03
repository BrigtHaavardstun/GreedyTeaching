import random
import networkx as nx
from networkx.algorithms import bipartite
from collections import defaultdict

W_tag = "w_"
C_tag = "c_"


def generate_graph(edge_list, witness_weight, concept_weight, max_weight=float("inf")):
    B = nx.Graph()
    concepts = set([c for (c, w) in edge_list])
    witness = set(
        [w for (c, w) in edge_list])

    B.add_nodes_from([c for c in concepts], bipartite=0)
    B.add_nodes_from([w for w in witness], bipartite=1)

    for (c, w) in edge_list:
        if (witness_weight[w] - concept_weight[c]) <= max_weight:
            B.add_edge(c, w)
    return B


def max_bipartite_matching(graph, return_matching=False):
    matching = nx.bipartite.maximum_matching(
        graph, top_nodes=get_concepts(graph))
    # divid by two becuse we list both c0 -> w1 and w1 -> c0
    if return_matching:
        return matching
    return len(matching) // 2


def get_concepts(graph):
    global C_tag
    return [node for node in graph.nodes() if node.startswith(C_tag)]


def get_witnesses(graph):
    global W_tag
    return [node for node in graph.nodes() if node.startswith(W_tag)]


def add_tags_edge_list(edge_list):
    global C_tag, W_tag
    return [(C_tag+str(concept), W_tag+str(witness)) for (concept, witness) in edge_list]


if __name__ == '__main__':
    edge_list = [(0, 1), (1, 0), (0, 2), (1, 2), (2, 3), (3, 0)]
    edge_list = add_tags_edge_list(edge_list)
    graph = generate_graph(
        edge_list, {W_tag + str(i): i for i in range(100)}, 1)
    print(max_bipartite_matching(graph))
    # print(get_witnesses(graph))
    # print(get_concepts(graph))
