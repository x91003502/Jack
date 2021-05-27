from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge

def find_sink(G, v):
    n_edge = len(G[v])
    for e in G[v]:
        w, weight = e[0], e[1]
        if w in G:
            return find_sink(G, w)
        else:
            n_edge -= 1
            print(f'vertex {w} is not in the graph')
    
    if n_edge == 0:
        del G[v]
        print(f'sink is found vertex {v} is deleted from the graph')
        return v

def naive_topological_sort(G, src):
    l = list()
    while len(G) > 0:
        l.append(find_sink(G, src))
    return l

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')

add_edge(G, 'a', 'b')
add_edge(G, 'b', 'c')
add_edge(G, 'c', 'd')

add_edge(G, 'a', 'd')

add_edge(G, 'a', 'e')
add_edge(G, 'e', 'd')
print(naive_topological_sort(G, 'a'))

# %% Topological sort using dfs
from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.dfs2 import DFS

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')

add_edge(G, 'a', 'b')
add_edge(G, 'b', 'c')
add_edge(G, 'c', 'd')

add_edge(G, 'a', 'd')

add_edge(G, 'a', 'e')
add_edge(G, 'e', 'd')

def dfs_topological_sort(G):
    _, post = DFS(G)
    l = list()
    for k in post:
        l.append(k)
    return l
print(dfs_topological_sort(G))