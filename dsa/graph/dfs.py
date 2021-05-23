from collections import defaultdict
from dsa.graph.depth_first_explore import depth_first_explore
from dsa.graph.graph_representation import add_vertex, add_edge, print_graph

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