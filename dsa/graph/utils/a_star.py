import math

def euclidean_distance(Map, v, t):
    v_pos = Map[v]
    t_pos = Map[t]
    vx, vy = v_pos[0], v_pos[1]
    tx, ty = t_pos[0], t_pos[1]
    return math.sqrt((vx-tx) ** 2 + (vy-ty) ** 2)

def manhattan_distance(Map, v, t):
    v_pos = Map[v]
    t_pos = Map[t]
    vx, vy = v_pos[0], v_pos[1]
    tx, ty = t_pos[0], t_pos[1]
    return abs(vx-tx) + abs(vy-ty)

def potential_edge_weight(edge_wegiht, Map, u, v, t, potential_function='euclidean_distance'):
    if potential_function == 'euclidean_distance':
        new_edge_weight = edge_wegiht - euclidean_distance(Map, u, t) + euclidean_distance(Map, v, t)
    elif potential_function == 'manhattan_distance':
        new_edge_weight = edge_wegiht - manhattan_distance(Map, u, t) + manhattan_distance(Map, v, t)
    return new_edge_weight

import sys
import heapq
def a_star(G, Map, s, t):
    dist, prev, proc = init_shortest_path(G, s)
    
    pq = init_pq(dist)
    
    while proc.get(t) is False:
        # If v pop from heap is already processed before, ignore it and pop again.
        distance, v = extract_min(pq, proc)
        print(f'found minimum score vertex {v} with score : {distance}')
        
        for e in G[v]:
            w, weight = e[0], e[1]
            new_dist = dist[v] + weight
            if new_dist < dist[w]:
                old_dist = dist[w]
                dist[w] = new_dist
                # update the new estimate distance of a vertex by adding a new item in heap
                # because the new distance must be smaller than previous, it will on the upper of the heap
                # and will be obtained before the old distance.
                new_score = new_dist - euclidean_distance(Map, s, t) +  euclidean_distance(Map, w, t)
                heapq.heappush(pq, (new_score, w))
                prev[w] = v
                print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
        proc[v] = True
    return dist

def init_shortest_path(G, s):
    dist, prev, proc = dict(), dict(), dict()
    for v in G:
        dist[v] = sys.maxsize
        prev[v] = None
        proc[v] = False
    dist[s] = 0
    return dist, prev, proc

import heapq
def init_pq(dist):
    pq = list()
    for v in dist:
        pq.append((dist[v], v))
    heapq.heapify(pq)
    return pq

def extract_min(pq, proc):
    while True:
        tup = heapq.heappop(pq)
        distance, v = tup[0], tup[1]
        if proc.get(v) is False:
            break
    return distance, v