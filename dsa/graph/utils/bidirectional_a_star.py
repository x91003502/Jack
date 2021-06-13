from collections import defaultdict, OrderedDict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.reverse_graph import reverse_graph
from dsa.graph.utils.a_star import compute_distance
from dsa.graph.utils.birectional_dijkstra import init_shortest_path, init_pq, extract_min, process, find_shortest_path

def bidirectional_a_star(G, Map, s, t, heuristic='euclidean'):
    GR = reverse_graph(G)
    
    G = compute_potential(G, Map, s, t, heuristic=heuristic)
    GR = compute_potential(GR, Map, t, s, heuristic=heuristic)
    
    dist, prev, proc = init_shortest_path(G, s)
    distR, prevR, procR = init_shortest_path(GR, t)
    
    pq = init_pq(dist)
    pqR = init_pq(distR)
    
    explore_record = OrderedDict()
    explore_recordR = OrderedDict()
    
    while True:
        distance, v = extract_min(pq, proc)
        process(v, G, pq, dist, prev, proc, explore_record)
        if procR.get(v) is True:
            print('forward and backward meet')
            break
        distanceR, vR = extract_min(pqR, procR)
        process(vR, GR, pqR, distR, prevR, procR, explore_recordR)
        if proc.get(vR) is True:
            print('forward and backward meet')
            break
    
    shortest_path = find_shortest_path(s, dist, prev, proc, t, distR, prevR, procR)
    return explore_record, explore_recordR, shortest_path

def compute_potential(G, Map, s, t, heuristic='euclidean'):
    newG = defaultdict(str)
    for v in G:
        add_vertex(newG, v)
        for e in G[v]:
            w, weight = e[0], e[1]
            v_pentential = compute_distance(Map, v, t, heuristic=heuristic)
            v_pententialR = compute_distance(Map, v, s, heuristic=heuristic)
            w_pentential = compute_distance(Map, w, t, heuristic=heuristic)
            w_pententialR = compute_distance(Map, w, s, heuristic=heuristic)
            p = (v_pentential - v_pententialR)/2
            pR = (w_pentential - w_pententialR)/2
            new_weight = weight - p + pR
            add_edge(newG, v, w, new_weight)
    return newG
