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