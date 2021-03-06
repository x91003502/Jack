from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.ssc import naive_ssc

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')

add_edge(G, 'a', 'b')
add_edge(G, 'b', 'a')

add_edge(G, 'b', 'c')

naive_ssc(G)


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

naive_ssc(G)


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

naive_ssc(G)

# %%
from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.ssc import dfs_ssc

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')


add_edge(G, 'b', 'a')
add_edge(G, 'a', 'c')
add_edge(G, 'c', 'b')

add_edge(G, 'a', 'd')
add_edge(G, 'd', 'e')

dfs_ssc(G)
# %%
from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex, add_edge
from dsa.graph.utils.ssc import dfs_ssc2

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')
add_vertex(G, 'c')
add_vertex(G, 'd')
add_vertex(G, 'e')


add_edge(G, 'b', 'a')
add_edge(G, 'a', 'c')
add_edge(G, 'c', 'b')

add_edge(G, 'a', 'd')
add_edge(G, 'd', 'e')

dfs_ssc2(G)