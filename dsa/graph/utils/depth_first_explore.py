def depth_first_explore(G, visited, v):
    visited[v] = True
    print(f'mark vertex : "{v}" visited')
    if G[v]:
        for e in G[v]:
            w, weight = e[0], e[1]
            if visited[w] == False:
                print(f'try to explore vertex "{v}" neighbor : vertex "{w}"')
                depth_first_explore(G, visited, w)