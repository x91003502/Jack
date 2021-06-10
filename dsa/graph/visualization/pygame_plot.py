# https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle
import sys
import pygame

BACKGROUND = (209, 217, 217) #d1d9d9
GRID = (0, 87, 146) #005792
BLOCK = (159, 184, 173)
EXPLORED = (148, 208, 204) #94d0cc
DISCOVERED = (238, 196, 196) #eec4c4
START = (104, 176, 171)#bdd2b6
TARGET = (242, 145, 145) #f29191
PATH = (255, 237, 163)
BLOCKSIZE = 30

PLOT_EXPLORE = 10
PLOT_PATH = 10
plot_explore_event = pygame.USEREVENT + 1
plot_path_event = pygame.USEREVENT + 2

def plot(Map, blocks, explored, shortest_path, start, target, n_col, n_row):
    global SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
    WINDOW_HEIGHT = BLOCKSIZE * n_row
    WINDOW_WIDTH = BLOCKSIZE * n_col
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BACKGROUND)
    
    pygame.time.set_timer(plot_explore_event, PLOT_EXPLORE)
    pygame.time.set_timer(plot_path_event, PLOT_PATH)
    
    x, y = Map[start]
    pos_x = BLOCKSIZE * x
    pos_y = BLOCKSIZE * y
    update_grid(pos_x, pos_y, action='start')
    
    x, y = Map[target]
    pos_x = BLOCKSIZE * x
    pos_y = BLOCKSIZE * y
    update_grid(pos_x, pos_y, action='target')
    
    for b in blocks:
        x, y = Map[b]
        pos_x = BLOCKSIZE * x
        pos_y = BLOCKSIZE * y
        update_grid(pos_x, pos_y, action='block')
    
    finish_explore = False
    explored_iter = iter(explored)
    path_iter = iter(shortest_path)
    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == plot_explore_event and finish_explore != True:
                v = next(explored_iter, None)
                if v == None:
                    finish_explore = True
                    continue
                if v == start : continue
                if v != target:
                    x, y = Map[v]
                    pos_x = BLOCKSIZE * x
                    pos_y = BLOCKSIZE * y
                    update_grid(pos_x, pos_y, action='explored')
                
                for w in explored[v]:
                    if w == target: continue
                    x, y = Map[w]
                    pos_x = BLOCKSIZE * x
                    pos_y = BLOCKSIZE * y
                    update_grid(pos_x, pos_y, action='discovered')
            if event.type == plot_path_event and finish_explore == True:
                v = next(path_iter, None)
                if v == None:
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()
                x, y = Map[v]
                pos_x = BLOCKSIZE * x
                pos_y = BLOCKSIZE * y
                update_grid(pos_x, pos_y, action='path')
                pygame.time.set_timer(plot_path_event, PLOT_PATH)
                
        pygame.display.update()

def draw_grid():
    global BLOCKSIZE
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GRID, rect, 1)

def update_grid(x, y, action):
    global BLOCKSIZE
    rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
    if action == 'start':
        pygame.draw.rect(SCREEN, START, rect, 0)
    elif action == 'target':
        pygame.draw.rect(SCREEN, TARGET, rect, 0)
    elif action == 'explored':
        pygame.draw.rect(SCREEN, EXPLORED, rect, 0)
    elif action == 'discovered':
        pygame.draw.rect(SCREEN, DISCOVERED, rect, 0)
    elif action == 'path':
        pygame.draw.rect(SCREEN, PATH, rect, 0)
    elif action == 'block':
        pygame.draw.rect(SCREEN, BLOCK, rect, 0)