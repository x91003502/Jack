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
