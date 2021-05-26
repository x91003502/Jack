from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.reverse_graph import reverse_graph

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')

add_edge(G, 'a', 'b')
add_edge(G, 'a', 'd')

add_edge(G, 'b', 'a')
add_edge(G, 'b', 'c')

add_edge(G, 'c', 'd')
add_edge(G, 'c', 'a')

add_edge(G, 'd', 'c')

print(G)

GR = reverse_graph(G)
print(GR)

