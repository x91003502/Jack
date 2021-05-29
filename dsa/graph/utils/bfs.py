from collections import deque
def BFS(G, s):
    dist = dict()
    for v in G:
        dist[v] = -1
    dist[s] = 0
    
    q = deque()
    q.append(s)
    while len(q) > 0:
        v = q.popleft()
        for e in G[v]:
            w, weight = e[0], e[1]
            if dist[w] == -1:
                print(f'discover vertex "{w}" in graph')
                q.append(w)
                dist[w] = dist[v] + 1
    return dist


def BFS2(G, s):
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
            if dist[w] == -1:
                print(f'discover vertex "{w}" in graph')
                q.append(w)
                dist[w] = dist[v] + 1
                prev[w] = v
    return dist, prev

def BFS_path(G, s, u):
    _, prev = BFS2(G, s)
    path = list()
    v = u
    while v is not None:
        path.append(v)
        v = prev[v]
    return reverse_list(path)

def reverse_list(l):
    i = 0
    j = len(l) - 1
    while i < j:
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        i += 1
        j -= 1
    return l