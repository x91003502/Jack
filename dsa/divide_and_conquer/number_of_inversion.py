# %%
import math
import numpy as np
def inversion(n, aux, arr, lo, mid, hi):
    print(f'from {lo} to {hi}')
    for i in range(lo, hi+1):
        aux[i] = arr[i]
    i = lo
    j = mid+1
    maxi = mid
    maxj = hi
    for k in range(lo, hi+1): # k = lo:hi inclusively
        # case 1
        if i > maxi and j <= maxj:
            arr[k] = aux[j]
            j += 1
            k += 1
            continue
        # case 2
        if i <= maxi and j > maxj:
            arr[k] = aux[i]
            i += 1
            k += 1
            continue
        # case 3
        if i <= maxi and j <= maxj:
            if aux[i] <= aux[j]:
                arr[k] = aux[i]
                i += 1
                k += 1
                continue
            else:
                for ii in range(i, maxi+1):
                    n += 1
                    print(f'inverse pair {aux[ii]} {aux[j]}')
                arr[k] = aux[j]
                j += 1
                k += 1
                continue
    print(f'n inversion : {n}')
    print(f'array : {arr}')

def recur_inversion(n, aux, arr, lo, hi):
    if hi > lo:
        mid = math.floor((lo+hi)/2)
        recur_inversion(n, aux, arr, lo, mid)
        recur_inversion(n, aux, arr, mid+1, hi)
        print(f'a: from {lo} to {mid}    b: from {mid+1} to {hi}')
        inversion(n, aux, arr, lo, mid, hi)

arr = [1,3,5,2,4]
arr = [2,3,9,2,9]
aux = np.zeros(len(arr))
lo = 0
hi = len(arr)-1
n = 0
recur_inversion(n, aux, arr, lo, hi)