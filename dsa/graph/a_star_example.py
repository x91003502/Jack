from collections import defaultdict
from dsa.graph.utils.graph_representation import add_vertex_2d, add_edge, add_vertex
from dsa.graph.utils.a_star import a_star, a_star2

def grid_2d(n_row, n_col, weight1=1, weight2=1.5):
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
            # if y+1 < n_row:
            #     ngbr_idx1 = x + n_col * (y+1) # upper
            #     add_edge(G, f'v{idx}', f'v{ngbr_idx1}', weight=weight1)
            # if x+1 < n_col:
            #     ngbr_idx3 = (x+1) + n_col * (y) # right
            #     add_edge(G, f'v{idx}', f'v{ngbr_idx3}', weight=weight1)
            # if y-1 >= 0:
            #     ngbr_idx5 = x + n_col * (y-1) # lower
            #     add_edge(G, f'v{idx}', f'v{ngbr_idx5}', weight=weight1)
            # if x-1 >= 0:
            #     ngbr_idx7 = (x-1) + n_col * (y) # left
            #     add_edge(G, f'v{idx}', f'v{ngbr_idx7}', weight=weight1)
            
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

import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

def draw(n_row, n_col, explored):
    grid = np.zeros((n_row, n_col))
    cmap = colors.ListedColormap(['Blue','red','yellow','green'])
    plt.figure(figsize=(6,6))
    plt.pcolor(grid[::1],cmap=cmap,edgecolors='k', linewidths=3)
    
    for v in explored:
        # mark source and target
        sx, sy = Map[start]
        grid[sy, sx] = 3
        tx, ty = Map[target]
        grid[ty, tx] = 3
        # explored vertex
        x, y = Map[v]
        grid[y, x] = 1
        
        for w in explored[v]:
            x, y = Map[w]
            grid[y, x] = 2
        plt.pcolor(grid[::1],cmap=cmap,edgecolors='k', linewidths=3)
        plt.draw()
        plt.pause(0.001)
    plt.pause(1)
    print(f'explore {len(explored)}')


n_col = 15
n_row = 15
G, Map = grid_2d(n_row, n_col, weight1=1, weight2=1.5)

start = 'v199'
target = 'v1'
# target = 'v222'
# explored = a_star(G, Map, start, target, heuristic='manhattan')
# explored = a_star(G, Map, start, target, heuristic='euclidean')

# explored = a_star2(G, Map, start, target, heuristic='manhattan')
explored = a_star2(G, Map, start, target, heuristic='euclidean')
# explored = a_star2(G, Map, start, target, heuristic='chebyshev')
draw(n_row, n_col, explored)