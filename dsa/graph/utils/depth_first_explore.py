def recur_depth_first_explore(G, visited, v, l):
    visited[v] = True
    l.append(v)
    print(f'mark vertex : "{v}" visited')
    if G[v]:
        for e in G[v]:
            w, weight = e[0], e[1]
            if visited[w] == False:
                print(f'try to explore vertex "{v}" neighbor : vertex "{w}"')
                recur_depth_first_explore(G, visited, w, l)
    # l = list()
    # for u in visited:
    #     if visited[u] is True:
    #         l.append(u)
    #     else: continue
    # return l

def depth_first_explore(G, visited, v):
    l = list()
    recur_depth_first_explore(G, visited, v, l)
    return l