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

from dsa.graph.utils.dfs2 import DFS
from dsa.graph.utils.reverse_graph import reverse_graph
def dfs_ssc(G):
    n_cc = 1
    GR = reverse_graph(G)
    while len(GR) > 0:
        _, post = DFS(GR)
        print(post)
        sink = max(post, key=post.get) # source of GR == sink of G
        print(f'sink : {sink} ')
        
        visited1 = dict()
        for w in GR:
            visited1[w] = False
        
        visited_list = depth_first_explore(G, visited1, sink)
        print(f'No. {n_cc} connected component {visited_list}')
        for v in visited_list:
            del GR[v]
        
        G = reverse_graph(GR) # update G, so no point to deleted vertices
        n_cc += 1

def dfs_ssc2(G):
    GR = reverse_graph(G)
    
    _, post = DFS(GR)

    n_cc = 1
    visited = dict()
    post_list = list()
    # the last item in the post(dictionary) must have the largest postvisit number
    # larger postvisit number, later insert into the dictionary
    # prove ?
    for v in post:
        post_list.append(v)
        visited[v] = False
    print(f'post order : {post_list}')
    
    for i in reversed(range(0, len(post_list))):
        v = post_list[i]
        if visited[v] is False:
            visited_list = depth_first_explore(G, visited, v)
            print(f'No. {n_cc} connected component {visited_list}')
            n_cc += 1