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

def diagonal_distance(Map, v, t, mode='chebyshev'):
    if mode =='chebyshev':
        D1 = 1
        D2 = 1
    v_pos = Map[v]
    t_pos = Map[t]
    vx, vy = v_pos[0], v_pos[1]
    tx, ty = t_pos[0], t_pos[1]
    dx, dy = abs(vx-tx), abs(vy-ty)
    return D1 * (dx + dy) - (D2 - 2 * D1) * min(dx, dy)

import sys
import heapq
def a_star(G, Map, s, t, heuristic='euclidean'):
    dist, prev, proc = init_shortest_path(G, s)
    
    pq = init_pq(dist)
    
    while proc.get(t) is False:
        distance, v = extract_min(pq, proc)
        print(f'found minimum score vertex {v} with score : {distance}')
        
        for e in G[v]:
            w, weight = e[0], e[1]
            new_dist = dist[v] + weight
            if new_dist < dist[w]:
                old_dist = dist[w]
                dist[w] = new_dist # store the new estimate value, SHOULD NOT adding this by the estimate distance to the target
                # dist[w] = new_dist + euclidean_distance(Map, w, t) # This is problematic
                if heuristic == None:
                    potential = new_dist
                elif heuristic == 'euclidean':
                    potential = new_dist + euclidean_distance(Map, w, t)
                elif heuristic == 'manhattan':
                    potential = new_dist + manhattan_distance(Map, w, t)
                elif heuristic == 'chebyshev':
                    print('chebyshev')
                    potential = new_dist + diagonal_distance(Map, w, t, mode='chebyshev')
                
                # update the new estimate distance of a vertex by adding a new item in heap
                # because the new distance must be smaller than previous, it will on the upper of the heap
                # and will be obtained before the old distance.
                heapq.heappush(pq, (potential, w)) # pushing the potential of a vertex in pq instead
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
    # If v pop from heap is already processed before, ignore it and pop again.
    while True:
        tup = heapq.heappop(pq)
        distance, v = tup[0], tup[1]
        if proc.get(v) is False:
            break
    return distance, v