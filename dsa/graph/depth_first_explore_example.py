from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.depth_first_explore import depth_first_explore

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