# naive implementaion
import sys
import numpy as np
def compute_dists(min_dist, arr, lo, hi):
    for i in range(lo, hi):
        p1 = arr[i]
        for j in range(i+1, hi+1):
            p2 = arr[j]
            dist = np.linalg.norm(p1 - p2)
            print(f'i {i}  j {j}  dist {dist}')
            if dist < min_dist:
                min_dist = dist
                print(f'new min_dist found  value {min_dist}')
    return min_dist


arr = [np.array((1,0)),np.array((4,0)),np.array((8,0)),np.array((9,0))]
min_dist = sys.maxsize
min_dist = compute_dists(min_dist, arr, 0, len(arr)-1)

# %% divide and conquer
import sys
import numpy as np
def compute_dists(min_dist, arr, lo, hi):
    for i in range(lo, hi):
        p1 = arr[i]
        for j in range(i+1, hi+1):
            p2 = arr[j]
            dist = np.linalg.norm(p1 - p2)
            print(f'i {i}  j {j}  dist {dist}')
            if dist < min_dist:
                min_dist = dist
                print(f'new min_dist found  value {min_dist}')
    return min_dist


import math
def divide(arr, lo, hi):
    if hi > lo:
        mid = math.floor((lo+hi)/2)
        dist1 = divide(arr, lo, mid)
        dist2 = divide(arr, mid+1, hi)
        min_dist = min(dist1, dist2)
        min_dist = compute_dists(min_dist, arr, lo, hi)
        return min_dist
    elif lo == hi:
        return sys.maxsize
print('================== Divide and Conquer ==================')
arr = [np.array((1,0)),np.array((4,0)),np.array((8,0)),np.array((9,0))]
min_dist = divide(arr, 0, len(arr)-1)
# %%
# %% divide and conquer 2
import sys
import numpy as np
def x_range_mean(arr, lo, hi):
    print(f'compute x mean from {lo} to {hi}')
    sum = 0
    for i in range(lo, hi+1):
        # print(arr[i][0])
        sum += arr[i][0]
    mean = sum/(hi-lo+1)
    x_mid_line = np.array((mean, 0))
    print(f'x_mid_line: {x_mid_line}')
    return x_mid_line

def x_narrow_search(min_dist, x_mid_line, arr, lo, hi):
    l = list()
    for i in range(lo, hi+1):
        dist_to_x = np.linalg.norm(arr[i] - x_mid_line)
        print(f'distance between {arr[i]} to x_mid_line is {dist_to_x}')
        if dist_to_x <= min_dist:
            l.append(i)
    if len(l) != 0:
        newlo = l[0]
        newhi = l[-1]
        print(f'newlo {newlo}  newhi {newhi}')
    else:
        newlo, newhi = -1, -1
    return newlo, newhi

def compute_dists(min_dist, arr, lo, hi):
    if lo == -1 and hi == -1:
        print('no update')
    for i in range(lo, hi):
        p1 = arr[i]
        for j in range(i+1, hi+1):
            p2 = arr[j]
            dist = np.linalg.norm(p1 - p2)
            print(f'i {i}  j {j}  dist {dist}')
            if dist < min_dist:
                min_dist = dist
                print(f'new min_dist found  value {min_dist}')
    return min_dist


import math
def divide(arr, lo, hi):
    if hi > lo:
        mid = math.floor((lo+hi)/2)
        dist1 = divide(arr, lo, mid)
        dist2 = divide(arr, mid+1, hi)
        min_dist = min(dist1, dist2)
        
        x_mid_line = x_range_mean(arr, lo, hi)
        newlo, newhi = x_narrow_search(min_dist, x_mid_line, arr, lo, hi)
        min_dist = compute_dists(min_dist, arr, newlo, newhi)
        return min_dist
    elif lo == hi:
        return sys.maxsize
print('================== Divide and Conquer ==================')
arr = [np.array((1,0)),np.array((4,0)),np.array((8,0)),np.array((9,0))]
min_dist = divide(arr, 0, len(arr)-1)
print(min_dist)