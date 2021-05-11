# Modify binary search for range search

import sys
import math
def binary_search_lower_bound(arr, target):
    lo = 0
    hi = len(arr)-1
    mid = math.floor((lo+hi)/2)
    cand_idx = mid
    # cand_idx = 0
    diff = sys.maxsize
    while hi >= lo:
        mid = math.floor((lo+hi)/2)
        if target == arr[mid]:
            return mid
         # update candiate
        elif target < arr[mid]:
            hi = mid-1
        else:
            lo = mid+1
            curr_diff = abs(arr[mid]-target)
            cand_idx = mid
            diff = curr_diff
    return cand_idx

def binary_search_upper_bound(arr, target):
    lo = 0
    hi = len(arr)-1
    cand_idx = len(arr)-1
    diff = sys.maxsize
    while hi >= lo:
        mid = math.floor((lo+hi)/2)
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            hi = mid-1
            curr_diff = abs(arr[mid]-target)
            cand_idx = mid
            diff = curr_diff
        else:
            lo = mid+1
    return cand_idx

arr = [1,6,11]
# arr = [-100,0,100]
index1 = binary_search_upper_bound(arr, 7)
print(f'index1 : {index1}')
index2 = binary_search_lower_bound(arr, 10)
print(f'index1 : {index1} index2 : {index2}')
    