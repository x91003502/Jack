
from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.shortest_path import bellman_ford

G = defaultdict(str)
add_vertex(G, 'S')
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')



add_edge(G, 'S', 'a', weight=4)
add_edge(G, 'S', 'b', weight=3)

add_edge(G, 'a', 'b', weight=-2)
add_edge(G, 'a', 'c', weight=4)

add_edge(G, 'b', 'c', weight=-3)
add_edge(G, 'b', 'd', weight=1)

add_edge(G, 'c', 'd', weight=2)

answer = [0, 4, 2, -1, 1]
dist = bellman_ford(G, 'S')
index = 0
for key in dist:
    assert dist[key] == answer[index]
    index += 1