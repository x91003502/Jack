from dsa.graph.utils.depth_first_explore import depth_first_explore

def DFS(G):
    visited = dict()
    
    # mark all vertices unvisited
    for v in G:
        visited[v] = False
        print(f'mark vertex : "{v}" unvisited')
    n_cc = 0 # number of connected components
    for v in G:
        if visited[v] == False:
            n_cc += 1
            print(f'try to explore vertex "{v}"')
            depth_first_explore(G, visited, v)
    print(f'\n{n_cc} connected components')