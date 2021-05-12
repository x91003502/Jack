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
    # target should be equal or higher than lower bound arr[cand_idx]
    if target >= arr[cand_idx]:
        return cand_idx
    else: return -1
    

def binary_search_upper_bound(arr, target):
    lo = 0
    hi = len(arr)-1
    cand_idx = len(arr)-1
    while hi >= lo:
        mid = math.floor((lo+hi)/2)
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            hi = mid-1
            curr_diff = abs(arr[mid]-target)
            cand_idx = mid
        else:
            lo = mid+1
    # target should be equal or less than upper bound arr[cand_idx]
    if target <= arr[cand_idx]:
        return cand_idx
    else: return sys.maxsize

def range_search(arr, range):
    # arr should be sorted
    index1 = binary_search_upper_bound(arr, range[0])
    index2 = binary_search_lower_bound(arr, range[1])
    # print(f'index1 : {index1} index2 : {index2}') 
    if index1 <= index2:
        print('in range')
    return index1, index2

# print(range_search([-100,10,100],[-10,10]))

