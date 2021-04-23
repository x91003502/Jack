# %%
import math
def divide_and_find(arr, lo, hi):
    if hi > lo:
        mid = math.floor((lo+hi)/2)
        # divide(arr, lo, mid)
        # divide(arr, mid+1, hi)
        val1, count1 = divide(arr, lo, mid)
        val2, count2 = divide(arr, mid+1, hi)
        print(f'a: from {lo} to {mid}    b: from {mid+1} to {hi}')
        # search another part
        for i in range(mid+1, hi+1):
            if val1 == arr[i]:
                count1 += 1
        for j in range(lo, mid+1): # j=0:mid inclusively
            if val2 == arr[j]:
                count2 += 1
        if count1 >= count2:
            return val1, count1
        else:
            return val2, count2
    else:
        val = arr[lo]
        count = 1
        return val, count
def majority_element(arr):
    lo = 0
    hi = len(arr)-1
    mid = math.ceil(len(arr)/2)
    val, count = divide(arr, lo, hi)
    if count >= mid:
        print(f'majority element is {val}, has {count} numbers of it.')
        return val
    else:
        print('no majority element is found')
        return 0

arr = [2,3,9,2,2,9,9,9,3,3,3,3,3,3]
majority_element(arr)