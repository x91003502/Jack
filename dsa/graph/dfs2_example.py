from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.dfs2 import DFS, pre, post

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