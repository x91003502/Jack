from collections import defaultdict
from dsa.graph.graph_representation import add_vertex, add_edge, print_graph
def depth_first_explore(G, visited, v):
    visited[v] = True
    print(f'mark vertex : "{v}" visited')
    if G[v]:
        for e in G[v]:
            w, weight = e[0], e[1]
            if visited[w] == False:
                print(f'try to explore vertex "{v}" neighbor : vertex "{w}"')
                depth_first_explore(G, visited, w)

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')


add_edge(G, 'a', 'b')
add_edge(G, 'b', 'a')

add_edge(G, 'b', 'c')
add_edge(G, 'c', 'b')

add_edge(G, 'c', 'd')
add_edge(G, 'd', 'c')


add_edge(G, 'd', 'e')
add_edge(G, 'e', 'd')

# print_graph(G)

visited = dict()
visited['a'] = False
visited['b'] = False
visited['c'] = False
visited['d'] = False
visited['e'] = False


depth_first_explore(G, visited, 'a')