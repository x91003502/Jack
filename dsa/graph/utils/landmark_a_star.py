from collections import defaultdict, OrderedDict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.reverse_graph import reverse_graph
from dsa.graph.utils.a_star import compute_distance
from dsa.graph.utils.a_star import init_shortest_path, init_pq, extract_min, process, find_shortest_path
from dsa.graph.utils.shortest_path import dijkstra2


def search_on_landmarks(G, GR, landmarks):
    dist_list = list()
    distR_list = list()
    for A in landmarks:
        dist = dijkstra2(G, A)
        distR = dijkstra2(GR, A)
        dist_list.append(dist)
        distR_list.append(distR)
    return dist_list, distR_list

def compute_potential(G, dist_list, distR_list, s, t):
    newG = defaultdict(str)
    # dist_iter = iter(dist_list)
    # distR_iter = iter(distR_list)
    for v in G:
        add_vertex(newG, v)
        for e in G[v]:
            w, weight = e[0], e[1]
            new_weight = 0
            for dist, distR in zip(dist_list, distR_list):
                piv = dist[t] - dist[v]
                piw = dist[t] - dist[w]
                # piv = max(dist[t] - dist[v], distR[v] - distR[t])
                # piw = max(dist[t] - dist[w], distR[w] - distR[t])
                if weight - piv + piw > new_weight:
                    new_weight = weight - piv + piw
            add_edge(newG, v, w, new_weight)
    return newG