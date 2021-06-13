from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex_2d, add_edge

def grid_2d_direction_4(n_row, n_col, weight1=1, weight2=1.5):
    G = defaultdict(str)
    Map = defaultdict(list)
    idx = 0
    
    # add vertices
    for y in range(0, n_row):
        for x in range(0, n_col):
            add_vertex_2d(G, f'v{idx}', Map, x, y)
            idx += 1
    
    # add edges
    for y in range(0, n_row):
        for x in range(0, n_col):
            idx = x + n_col * y
            if y+1 < n_row:
                ngbr_idx1 = x + n_col * (y+1) # upper
                add_edge(G, f'v{idx}', f'v{ngbr_idx1}', weight=weight1)
            if x+1 < n_col:
                ngbr_idx3 = (x+1) + n_col * (y) # right
                add_edge(G, f'v{idx}', f'v{ngbr_idx3}', weight=weight1)
            if y-1 >= 0:
                ngbr_idx5 = x + n_col * (y-1) # lower
                add_edge(G, f'v{idx}', f'v{ngbr_idx5}', weight=weight1)
            if x-1 >= 0:
                ngbr_idx7 = (x-1) + n_col * (y) # left
                add_edge(G, f'v{idx}', f'v{ngbr_idx7}', weight=weight1)
    return G, Map

def grid_2d_direction_8(n_row, n_col, weight1=1, weight2=1.5):
    G = defaultdict(str)
    Map = defaultdict(list)
    idx = 0
    
    # add vertices
    for y in range(0, n_row):
        for x in range(0, n_col):
            add_vertex_2d(G, f'v{idx}', Map, x, y)
            idx += 1
    
    # add edges
    for y in range(0, n_row):
        for x in range(0, n_col):
            idx = x + n_col * y  
            if y+1 < n_row:
                ngbr_idx1 = x + n_col * (y+1) # upper
                add_edge(G, f'v{idx}', f'v{ngbr_idx1}', weight=weight1)
            if x+1 < n_col and y+1 < n_row:
                ngbr_idx2 = (x+1) + n_col * (y+1) # upper right
                add_edge(G, f'v{idx}', f'v{ngbr_idx2}', weight=weight2)
            if x+1 < n_col:
                ngbr_idx3 = (x+1) + n_col * (y) # right
                add_edge(G, f'v{idx}', f'v{ngbr_idx3}', weight=weight1)
            if x+1 < n_col and y-1 >= 0:
                ngbr_idx4 = (x+1) + n_col * (y-1) # lower right
                add_edge(G, f'v{idx}', f'v{ngbr_idx4}', weight=weight2)
            if y-1 >= 0:
                ngbr_idx5 = x + n_col * (y-1) # lower
                add_edge(G, f'v{idx}', f'v{ngbr_idx5}', weight=weight1)
            if x-1 >= 0 and y-1 >= 0:
                ngbr_idx6 = (x-1) + n_col * (y-1) # lower left
                add_edge(G, f'v{idx}', f'v{ngbr_idx6}', weight=weight2)
            if x-1 >= 0:
                ngbr_idx7 = (x-1) + n_col * (y) # left
                add_edge(G, f'v{idx}', f'v{ngbr_idx7}', weight=weight1)
            if x-1 >=0 and y+1 < n_row:
                ngbr_idx8 = (x-1) + n_col * (y+1) # upper left
                add_edge(G, f'v{idx}', f'v{ngbr_idx8}', weight=weight2)
    return G, Map

def block(G, b):
    for e in G[b]:
        w1, weight2 = e[0], e[1]
        for v in G[w1]:
            w2, weight2 = v[0], v[1]
            if w2 == b:
                G[w1].remove([w2, weight2])
    del G[b]