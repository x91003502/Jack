from collections import defaultdict
# Implement graph data structure by Python dictionary
def add_vertex(G, v):
    if v in G:
        print(f'vertex "{v}" is already stored in graph')
    else:
        print(f'add vertex "{v}" in graph')
        G[v] = list()

def add_edge(G, v, u, weight=0):
    if v in G:
        edge = [u, weight]
        G[v].append(edge)
    else:
        print(f'vertex "{v}" is not stored in graph')

def print_graph(G):
    for v in G:
        print(f'Vertex : {v}')
        if G[v]:
            for e in G[v]:
                u, weight = e[0], e[1]
                print(f'    {v} -> {u}    |    edge weight : {weight}')
        else:
            print(f'    no edge')

G = defaultdict(str)
add_vertex(G, 'a')
add_vertex(G, 'b')

add_edge(G, 'a', 'b')
add_edge(G, 'a', 'c')

print_graph(G)

