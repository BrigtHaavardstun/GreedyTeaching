import networkx as nx
from networkx.algorithms import bipartite
from collections import defaultdict

W_tag = "w_"
C_tag = "c_"


def generate_graph(edge_list, witness_weight, maxWintessNr=float("inf")):
    B = nx.Graph()
    representations = set([c for (c, w) in edge_list])
    witness = set(
        [w for (c, w) in edge_list])

    B.add_nodes_from([c for c in representations], bipartite=0)
    B.add_nodes_from([w for w in witness], bipartite=1)

    for (c, w) in edge_list:
        if witness_weight[w] <= maxWintessNr:
            B.add_edge(c, w)
    return B


def get_size_of_max_bipartite_matching(graph, representaions):
    matching = nx.bipartite.maximum_matching(
        graph, top_nodes=representaions)
    # divid by two becuse we list both c0 -> w1 and w1 -> c0
    return len(matching) // 2


def get_max_bipartite_matching(graph, representaions):
    return nx.bipartite.maximum_matching(
        graph, top_nodes=representaions)
