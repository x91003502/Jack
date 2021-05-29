from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge

def reverse_graph(G):
    GR = defaultdict(str)
    for v in G:
        add_vertex(GR, v)
    for v in G:
        for e in G[v]:
            w, weight = e[0], e[1]
            add_edge(GR, w, v)
    return GR