import math
from dsa.graph.utils.birectional_dijkstra import init_shortest_path, init_pq, extract_min, process

def compute_distance(Map, v, t, heuristic='euclidean'):
    v_pos = Map[v]
    t_pos = Map[t]
    distance = float
    if heuristic == None:
        distance = 0
    elif heuristic == 'euclidean':
        distance = euclidean((v_pos[0], v_pos[1]), (t_pos[0], t_pos[1]))
    elif heuristic == 'manhattan':
        distance =manhattan((v_pos[0], v_pos[1]), (t_pos[0], t_pos[1]))
    elif heuristic == 'chebyshev':
        distance = chebyshev((v_pos[0], v_pos[1]), (t_pos[0], t_pos[1]))
    return distance

def euclidean(a, b):
    return math.sqrt((a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2)

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def chebyshev(a, b):
    D1 = 1
    D2 = 1
    dx, dy = abs(a[0]-b[0]), abs(a[1]-b[1])
    return D1 * max(dx, dy) + (D2-D1) * min(dx, dy)

import sys
import heapq
from collections import OrderedDict
# def a_star(G, Map, s, t, heuristic='euclidean'):
#     dist, prev, proc = init_shortest_path(G, s)
    
#     pq = init_pq(dist)
    
#     explore_record = OrderedDict()
    
#     while proc.get(t) is False:
#         distance, v = extract_min(pq, proc)
#         print(f'found minimum score vertex {v} with score : {distance}')
#         a_star_process(v, G, pq, dist, prev, proc, Map, t, heuristic, explore_record)
#     return explore_record

def a_star2(G, Map, s, t, heuristic='euclidean'):
    G = compute_potential(G, Map, t, heuristic=heuristic)
    # G = compute_potential2(G, Map, s, t, heuristic=heuristic)
    dist, prev, proc = init_shortest_path(G, s)
    
    pq = init_pq(dist)
    
    explore_record = OrderedDict()
    
    while proc.get(t) is False:
        distance, v = extract_min(pq, proc)
        print(f'found minimum score vertex {v} with score : {distance}')
        process(v, G, pq, dist, prev, proc, explore_record)
        proc[v] = True
    shortest_path = find_shortest_path(prev, s, t)
    return explore_record, shortest_path

def a_star3(G, Map, s, t, heuristic='euclidean'):
    # G = compute_potential(G, Map, t, heuristic=heuristic)
    G = compute_potential2(G, Map, s, t, heuristic=heuristic)
    dist, prev, proc = init_shortest_path(G, s)
    
    pq = my_init_pq(dist)
    
    explore_record = OrderedDict()
    
    while proc.get(t) is False:
        distance, v = my_extract_min(pq, proc)
        print(f'found minimum score vertex {v} with score : {distance}')
        my_process(v, G, pq, dist, prev, proc, explore_record)
    shortest_path = find_shortest_path(prev, s, t)
    return explore_record, shortest_path

# def a_star_process(v, G, pq, dist, prev, proc, Map, t, heuristic, explore_record):
    
#     explore_record[v] = list()
    
#     for e in G[v]:
#         w, weight = e[0], e[1]
#         new_dist = dist[v] + weight
#         if new_dist < dist[w]:
#             old_dist = dist[w]
#             dist[w] = new_dist # store the new estimate value, SHOULD NOT adding this by the estimate distance to the target
#             # dist[w] = new_dist + euclidean_distance(Map, w, t) # This is problematic
            
#             explore_record[v].append(w)
            
#             if heuristic == None:
#                 potential = new_dist
#             elif heuristic == 'euclidean':
#                 potential = new_dist + euclidean_distance(Map, w, t)
#             elif heuristic == 'manhattan':
#                 potential = new_dist + manhattan_distance(Map, w, t)
#             elif heuristic == 'chebyshev':
#                 print('chebyshev')
#                 potential = new_dist + diagonal_distance(Map, w, t, mode='chebyshev')
            
#             # update the new estimate distance of a vertex by adding a new item in heap
#             # because the new distance must be smaller than previous, it will on the upper of the heap
#             # and will be obtained before the old distance.
#             heapq.heappush(pq, (potential, w)) # pushing the potential of a vertex in pq instead
#             prev[w] = v
#             print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
#     proc[v] = True

from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
def compute_potential(G, Map, t, heuristic='euclidean'):
    newG = defaultdict(str)
    for v in G:
        add_vertex(newG, v)
        for e in G[v]:
            w, weight = e[0], e[1]
            v_pentential = compute_distance(Map, v, t, heuristic=heuristic)
            w_pentential = compute_distance(Map, w, t, heuristic=heuristic)
            new_weight = weight - v_pentential + w_pentential
            add_edge(newG, v, w, new_weight)
    return newG

def compute_potential2(G, Map, s, t, heuristic='euclidean'):
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

import heapq
def init_pq(dist):
    pq = list()
    for v in dist:
        pq.append((dist[v], v))
    heapq.heapify(pq)
    return pq

import sys
from dsa.basic_data_structures.priority_queue import PriorityQueue
class PQVertex(object):
    def __init__(self, id, distance):
        self.id = id
        self.distance = [distance]
    
    def get_id(self):
        return self.id
    
    def get_dist(self):
        return self.distance[0]

def my_init_pq(dist):
    capacity = 1000
    sortKey = 'distance'
    pq = PriorityQueue(capacity, sortKey=sortKey)
    l = list()
    # Not efficient way to build a heap
    for v in dist:
        pq_vertex = PQVertex(v, distance=dist[v])
        pq.insert(pq_vertex)
    return pq

def my_extract_min(pq, proc):
    while True:
        vertex = pq.removeMin()
        distance, v = vertex.get_dist(), vertex.get_id()
        if proc.get(v) is False:
            break
    return distance, v

def my_process(v, G, pq, dist, prev, proc, explore_record):
    
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
            pq_vertex = PQVertex(w, distance=new_dist)
            pq.insert(pq_vertex)
            prev[w] = v
            print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    proc[v] = True

def find_shortest_path(prev, start, target):
    shortest_path = list()
    curr = prev[target]
    while curr != start:
        shortest_path.append(curr)
        curr = prev[curr]
    return shortest_path