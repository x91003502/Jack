from collections import defaultdict, OrderedDict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.reverse_graph import reverse_graph
from dsa.graph.utils.a_star import compute_distance
from dsa.graph.utils.birectional_dijkstra import init_shortest_path, init_pq, extract_min, process, find_shortest_path

def landmark_a_star(G, Map, landmarks, s, t, heuristic='euclidean'):
    GR = reverse_graph(G)
    
    G = compute_potential(G, Map, landmarks, s, t, heuristic=heuristic)
    GR = compute_potential(GR, Map, landmarks, t, s, heuristic=heuristic)
    
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

def compute_potential(G, Map, landmarks, s, t, heuristic='euclidean'):
    newG = defaultdict(str)
    for v in G:
        add_vertex(newG, v)
        for e in G[v]:
            w, weight = e[0], e[1]
            edge_weight = 0
            for A in landmarks:
                dAt = compute_distance(Map, A, t, heuristic=heuristic)
                dAv = compute_distance(Map, A, v, heuristic=heuristic)
                
                dtA = compute_distance(Map, t, A, heuristic=heuristic)
                dvA = compute_distance(Map, v, A, heuristic=heuristic)
                
                piv = max(dAt-dAv, dvA-dtA)
                
                dAt = compute_distance(Map, A, t, heuristic=heuristic)
                dAw = compute_distance(Map, A, w, heuristic=heuristic)
                
                dtA = compute_distance(Map, t, A, heuristic=heuristic)
                dwA = compute_distance(Map, w, A, heuristic=heuristic)
                
                piw = max(dAt-dAw, dwA-dtA)
                
                new_weight = weight - piv + piw
                
                if new_weight > edge_weight:
                    edge_weight = new_weight
                    print(f'landmark "{A}" improve lower bound.  new_weight : {edge_weight}')
            add_edge(newG, v, w, edge_weight)
    return newG