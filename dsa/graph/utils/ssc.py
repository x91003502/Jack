from dsa.graph.utils.depth_first_explore import depth_first_explore

def naive_ssc(G):
    visited = dict()
    label = dict()
    # mark all vertices unvisited
    for u in G:
        visited[u] = False
        label[u] = -1
        # print(f'mark vertex : "{u}" unvisited')
    n_cc = 1
    
    for v in G:
        if visited[v] == False:
            ssc = list()
            
            visited1 = dict()
            for w in G:
                visited1[w] = False
            
            visited_list = depth_first_explore(G, visited1, v)
            
            for u in visited_list:
                visited2 = dict()
                for w in G:
                    visited2[w] = False
                
                visited_list2 = depth_first_explore(G, visited2, u)
                
                for w in visited_list2:
                    if w is v:
                        ssc.append(u)
                        label[u] = n_cc
                        visited[u] = True
            print(f'No. {n_cc} connected component {ssc}')
            n_cc += 1