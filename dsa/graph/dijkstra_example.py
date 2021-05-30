

from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.shortest_path import dijkstra, dijkstra2

G = defaultdict(str)
add_vertex(G, 'S')
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')

add_edge(G, 'S', 'a', weight=3)
add_edge(G, 'S', 'b', weight=10)

add_edge(G, 'a', 'c', weight=3)
add_edge(G, 'a', 'd', weight=5)
add_edge(G, 'a', 'b', weight=8)

add_edge(G, 'b', 'a', weight=2)
add_edge(G, 'b', 'd', weight=5)

add_edge(G, 'c', 'e', weight=2)
add_edge(G, 'c', 'd', weight=1)
add_edge(G, 'c', 'b', weight=3)

add_edge(G, 'd', 'e', weight=0)

dist1 = dijkstra(G, 'S')
dist2 = dijkstra2(G, 'S')
assert len(dist1) == len(dist2)
for v in dist1:
    assert dist1[v] == dist2[v]