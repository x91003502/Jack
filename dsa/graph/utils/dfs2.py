def depth_first_explore(G, visited, v, pre, post, clock):
    visited[v] = True
    print(f'mark vertex : "{v}" visited')
    previsit(v, pre, clock)
    if G[v]:
        for e in G[v]:
            w, weight = e[0], e[1]
            if visited[w] == False:
                print(f'try to explore vertex "{v}" neighbor : vertex "{w}"')
                depth_first_explore(G, visited, w, pre, post, clock)
    postvisit(v, post, clock)

def DFS(G):
    visited = dict()
    pre = dict()
    post = dict()
    clock = Clock()
    # mark all vertices unvisited
    for v in G:
        visited[v] = False
        print(f'mark vertex : "{v}" unvisited')
    n_cc = 0 # number of connected components
    
    for v in G:
        if visited[v] == False:
            n_cc += 1
            print(f'try to explore vertex "{v}"')
            depth_first_explore(G, visited, v, pre, post, clock)
    print(f'\n{n_cc} connected components')
    return pre, post

class Clock(object):
    def __init__(self, count = 1):
        self.count = count
    def increment(self):
        self.count += 1

# pre = dict()
# post = dict()
# clock = 1
def previsit(v, pre, clock):
    pre[v] = clock.count
    clock.increment()

def postvisit(v, post, clock):
    post[v] = clock.count
    clock.increment()

def is_valid_prepost(pre, post):
    '''
    Check if previst and postvist sets are valid in the "SAME" connected component.
    '''
    assert len(pre) == len(post)
    keys = list()
    for key in pre.keys():
        keys.append(key)
    for i in range(len(keys)):
        for j in range(i+1, len(pre)):
            k1 = keys[i]
            k2 = keys[j]
            if pre[k1] < pre[k2]:
                assert post[k1] > post[k2]
            elif pre[k1] > pre[k2]:
                assert post[k1] < post[k2]