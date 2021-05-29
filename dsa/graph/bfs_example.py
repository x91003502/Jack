from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.bfs import BFS_path

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')
add_vertex(G, 'f')
add_vertex(G, 'g')
add_vertex(G, 'h')
add_vertex(G, 'S')


add_edge(G, 'a', 'b')
add_edge(G, 'a', 'S')

add_edge(G, 'S', 'a')
add_edge(G, 'S', 'c')
add_edge(G, 'S', 'd')
add_edge(G, 'S', 'e')

add_edge(G, 'e', 'S')
add_edge(G, 'e', 'd')

add_edge(G, 'b', 'a')
add_edge(G, 'b', 'h')
add_edge(G, 'b', 'g')
add_edge(G, 'b', 'c')

add_edge(G, 'c', 'b')
add_edge(G, 'c', 'S')

add_edge(G, 'd', 'e')
add_edge(G, 'd', 'S')
add_edge(G, 'd', 'f')

add_edge(G, 'h', 'b')
add_edge(G, 'h', 'g')

add_edge(G, 'g', 'b')
add_edge(G, 'g', 'h')
add_edge(G, 'g', 'f')

add_edge(G, 'f', 'g')
add_edge(G, 'f', 'd')

#   e - S - a
#   | / |   |
#   d   c - b
#   |     / |
#   f - g - h


#   0 | 1 | 2 | 3
#===================
#             |-g
#   |-- a-- b-|
#   |         |-h
#   |-- c
#   S
#   |-- d-- f
#   |    
#   |-- e

assert BFS_path(G, 'S', 'a') == ['S', 'a']
assert BFS_path(G, 'S', 'c') == ['S', 'c']
assert BFS_path(G, 'S', 'd') == ['S', 'd']
assert BFS_path(G, 'S', 'e') == ['S', 'e']

assert BFS_path(G, 'S', 'b') == ['S', 'a', 'b']
assert BFS_path(G, 'S', 'f') == ['S', 'd', 'f']

assert BFS_path(G, 'S', 'g') == ['S', 'a', 'b', 'g']
assert BFS_path(G, 'S', 'h') == ['S', 'a', 'b', 'h']