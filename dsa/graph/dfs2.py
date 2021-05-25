from collections import defaultdict
from dsa.graph.graph_representation import add_vertex, add_edge, print_graph

def depth_first_explore(G, visited, v):
    visited[v] = True
    print(f'mark vertex : "{v}" visited')
    previsit(v)
    if G[v]:
        for e in G[v]:
            w, weight = e[0], e[1]
            if visited[w] == False:
                print(f'try to explore vertex "{v}" neighbor : vertex "{w}"')
                depth_first_explore(G, visited, w)
    postvisit(v)

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

pre = dict()
post = dict()
clock = 1
def previsit(v):
    global clock
    pre[v] = clock
    clock += 1

def postvisit(v):
    global clock
    post[v] = clock
    clock += 1

def is_valid_prepost(pre, post):
    '''
    Check if previst and postvist are valid in the "SAME" connected component.
    '''
    assert len(pre) == len(post)
    keys = list()
    for key in pre.keys():
        keys.append(key)
    for i in range(len(keys)):
        for j in range(i+1, len(pre)):
            k1 = keys[i]
            k2 = keys[j]
            if pre[k1] < pre[k2]:
                assert post[k1] > post[k2]
            elif pre[k1] > pre[k2]:
                assert post[k1] < post[k2]


G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')
add_vertex(G, 'f')



add_edge(G, 'a', 'b')
add_edge(G, 'b', 'a')

add_edge(G, 'b', 'c')
add_edge(G, 'c', 'b')

add_edge(G, 'a', 'c')
add_edge(G, 'c', 'a')


add_edge(G, 'd', 'e')
add_edge(G, 'e', 'd')


# graph
#        a              d       f
#      /   \            |
#    b  ---  c          e

DFS(G)
print(pre)
print(post)