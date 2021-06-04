import sys
from collections import deque

def naive_shortest_path(G, s):
    dist, prev = dict(), dict()
    for v in G:
        dist[v] = sys.maxsize
        prev[v] = None
    dist[s] = 0
    make_change = True
    
    while make_change:
        make_change = False
        for v in G:
            for e in G[v]:
                w, weight = e[0], e[1]
                new_dist = dist[v] + weight
                if new_dist < dist[w]:
                    make_change = True
                    old_dist = dist[w]
                    dist[w] = new_dist
                    prev[w] = v
                    print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    return dist

def bellman_ford(G, s):
    dist, prev = dict(), dict()
    for v in G:
        dist[v] = sys.maxsize
        prev[v] = None
    dist[s] = 0
    for i in range(1, len(G)): # i=1:|V|-1
        for v in G:
            for e in G[v]:
                w, weight = e[0], e[1]
                new_dist = dist[v] + weight
                if new_dist < dist[w]:
                    old_dist = dist[w]
                    dist[w] = new_dist
                    prev[w] = v
                    print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    
    # negative cycle detection
    has_neg_cycle = False
    nv = None # vertex that is reachable from a negative cycle
    for v in G:
        for e in G[v]:
            w, weight = e[0], e[1]
            new_dist = dist[v] + weight
            if new_dist < dist[w]:
                has_neg_cycle = True
                nv = w
                print(f'detect a negative cycle  vertex "{nv}" is reachable from the negative cycle')
    
    if has_neg_cycle is not True:
        return dist
    else:
        return find_negative_cycle(prev, nv)

def find_negative_cycle(prev, nv):
    start_vertex = nv
    v = nv
    neg_cycle = list()
    while True:
        neg_cycle.append(v)
        v = prev[v]
        if v == start_vertex:
            break
    return neg_cycle

def bfs_shortest_path(G, s):
    dist, prev = dict(), dict()
    for v in G:
        dist[v] = -1
        prev[v] = None
    dist[s] = 0
    
    q = deque()
    q.append(s)
    while len(q) > 0:
        v = q.popleft()
        for e in G[v]:
            w, weight = e[0], e[1]
            new_dist = dist[v] + weight
            
            if dist[w] == -1:
                q.append(w)
                dist[w] = new_dist
                prev[w] = v
                print(f'discover vertex "{w}" in graph')
            
            if new_dist < dist[w]:
                q.append(w)
                old_dist = dist[w]
                dist[w] = new_dist
                prev[w] = v
                print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    return dist

def dijkstra(G, s):
    dist, prev = dict(), dict()
    
    for v in G:
        dist[v] = sys.maxsize
        prev[v] = None
    dist[s] = 0
    unprocess = dist.copy()
    while len(unprocess) > 0:
        v = find_min_dist(unprocess)
        del unprocess[v]
        for e in G[v]:
            w, weight = e[0], e[1]
            new_dist = dist[v] + weight
            if new_dist < dist[w]:
                old_dist = dist[w]
                dist[w] = new_dist
                unprocess[w] = new_dist
                prev[w] = v
                print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    return dist

def compute_total_weight(G):
    total_weight = 0
    for v in G:
        for e in G[v]:
            w, weight = e[0], e[1]
            total_weight += weight
    return total_weight

def find_min_dist(dist):
    min_dist_value = sys.maxsize
    min_dist_vertex = None
    for v in dist:
        dist_value = dist[v]
        if dist_value < min_dist_value:
            min_dist_value = dist_value
            min_dist_vertex = v
    print(f'found minimum distance vertex {min_dist_vertex} with distance : {min_dist_value}')
    return min_dist_vertex

import heapq
def dijkstra2(G, s):
    dist, prev, unprocess = dict(), dict(), dict()
    
    for v in G:
        dist[v] = sys.maxsize
        prev[v] = None
        unprocess[v] = True
    dist[s] = 0
    pq = list()
    for v in dist:
        pq.append((dist[v], v))
    heapq.heapify(pq)
    
    while len(unprocess) > 0:
        # If v pop from heap is already processed before, ignore it and pop again.
        while True:
            tup = heapq.heappop(pq)
            distance, v = tup[0], tup[1]
            if v in unprocess:
                break
        print(f'found minimum distance vertex {v} with distance : {distance}')
        del unprocess[v]
        for e in G[v]:
            w, weight = e[0], e[1]
            new_dist = dist[v] + weight
            if new_dist < dist[w]:
                old_dist = dist[w]
                dist[w] = new_dist
                # update the new estimate distance of a vertex by adding a new item in heap
                # because the new distance must be smaller than previous, it will on the upper of the heap
                # and will be obtained before the old distance.
                heapq.heappush(pq, (new_dist, w))
                prev[w] = v
                print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    return dist