
from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.shortest_path import naive_shortest_path

G = defaultdict(str)
add_vertex(G, 'S')
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')



add_edge(G, 'a', 'd', weight=1)
add_edge(G, 'a', 'c', weight=1)
add_edge(G, 'a', 'S', weight=1)

add_edge(G, 'b', 'c', weight=1)
add_edge(G, 'b', 'S', weight=1)

add_edge(G, 'c', 'b', weight=1)
add_edge(G, 'c', 'a', weight=1)

add_edge(G, 'd', 'a', weight=1)

add_edge(G, 'S', 'a', weight=4)
add_edge(G, 'S', 'b', weight=1)


dist = naive_shortest_path(G, 'S')
print(dist)

G = defaultdict(str)
add_vertex(G, 's')
add_vertex(G, 't')
add_vertex(G, 'x')
add_vertex(G, 'y')
add_vertex(G, 'z')

add_edge(G, 's', 't', weight=6)
add_edge(G, 's', 'y', weight=7)

add_edge(G, 't', 'y', weight=8)
add_edge(G, 't', 'x', weight=5)
add_edge(G, 't', 'z', weight=-4)

add_edge(G, 'x', 't', weight=-2)

add_edge(G, 'y', 'z', weight=9)
add_edge(G, 'y', 'x', weight=-3)

add_edge(G, 'z', 'x', weight=2)
add_edge(G, 'z', 's', weight=7)

dist = naive_shortest_path(G, 's')





