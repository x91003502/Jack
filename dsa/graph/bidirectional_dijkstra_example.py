# from collections import defaultdict
# from dsa.graph.utils.graph_representation import add_vertex, add_edge
from typing import OrderedDict
from dsa.graph.utils.advanced_shortest_path import birectional_dijkstra

# G = defaultdict(str)
# add_vertex(G, 'S')
# add_vertex(G, 'a')
# add_vertex(G, 'b')
# add_vertex(G, 'c')
# add_vertex(G, 'd')
# add_vertex(G, 'e')

# add_edge(G, 'S', 'a', weight=3)
# add_edge(G, 'S', 'b', weight=10)

# add_edge(G, 'a', 'c', weight=3)
# add_edge(G, 'a', 'd', weight=5)
# add_edge(G, 'a', 'b', weight=8)

# add_edge(G, 'b', 'a', weight=2)
# add_edge(G, 'b', 'd', weight=5)

# add_edge(G, 'c', 'e', weight=2)
# add_edge(G, 'c', 'd', weight=1)
# add_edge(G, 'c', 'b', weight=3)

# add_edge(G, 'd', 'e', weight=0)

# birectional_dijkstra(G, 'S', 'e')

from dsa.graph.utils.init_gird import grid_2d_direction_4
n_col = 30
n_row = 30
G, Map = grid_2d_direction_4(n_row, n_col, weight1=1, weight2=1)
start = 'v0'
target = 'v888'


from collections import OrderedDict
def interleave(explore_record, explore_recordR):
    iterator = iter(explore_record)
    iteratorR = iter(explore_recordR)
    interleave_record = OrderedDict()
    while True:
        v = next(iterator, None)
        vR = next(iteratorR, None)
        if v != None:
            interleave_record[v] = explore_record[v]
        if vR != None:
            interleave_record[vR] = explore_recordR[vR]
        if v == None and vR == None:
            break
    return interleave_record

explore_record, explore_recordR, shortest_path = birectional_dijkstra(G, start, target)
interleave_record = interleave(explore_record, explore_recordR)
print(shortest_path)
from dsa.graph.visualization.pygame_plot import plot
plot(Map, interleave_record, shortest_path, start, target, n_col, n_row)