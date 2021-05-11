import math
def binary_search(target, arr, lo, hi):
    if hi > lo:
        mid = math.floor((lo+hi)/2)
        print(f'mid {mid}')
        if arr[mid] == target:
            print(f'target : {target} found')
            return mid
        else:
            binary_search(target, arr, lo, mid)
            binary_search(target, arr, mid+1, hi)
    if lo == len(arr):
        print(f'target : {target} not found')

arr = [1,3,7,8,9,12,15]
binary_search(11, arr, 0, len(arr))