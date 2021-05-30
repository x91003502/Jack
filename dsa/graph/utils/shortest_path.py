from collections import deque

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

import sys
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


import sys
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
                heapq.heappush(pq, (new_dist, w))
                prev[w] = v
                print(f'update distance of vertex "{w}" from {old_dist} to {new_dist}')
    return dist