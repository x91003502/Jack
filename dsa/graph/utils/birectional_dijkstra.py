import sys
from dsa.graph.utils.reverse_graph import reverse_graph
from collections import OrderedDict

def birectional_dijkstra(G, s, t):
    GR = reverse_graph(G)
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

def process(v, G, pq, dist, prev, proc, explore_record):
    
    explore_record[v] = list()
    
    for e in G[v]:
        w, weight = e[0], e[1]
        new_dist = dist[v] + weight
        if new_dist < dist[w]:
            old_dist = dist[w]
            dist[w] = new_dist
            
            explore_record[v].append(w)
            
            # update the new estimate distance of a vertex by adding a new item in heap
            # because the new distance must be smaller than previous, it will on the upper of the heap
            # and will be obtained before the old distance.
            heapq.heappush(pq, (new_dist, w))
            prev[w] = v
            print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    proc[v] = True

def find_shortest_path(s, dist, prev, proc, t, distR, prevR, procR):
    distance = sys.maxsize
    v_best = None
    for v in proc:
        new_dist = dist[v] + distR[v]
        if new_dist < distance:
            v_best = v
            distance = new_dist
    for v in procR:
        new_dist = dist[v] + distR[v]
        if new_dist < distance:
            v_best = v
            distance = new_dist
    
    path = list()
    curr_v = v_best
    while curr_v != s:
        path.append(curr_v)
        curr_v = prev[curr_v]
    path.reverse()
    
    curr_v = v_best
    while curr_v != t:
        if curr_v != v_best:
            path.append(curr_v)
        curr_v = prevR[curr_v]
    return path