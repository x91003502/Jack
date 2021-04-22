# %%
# Iterative method to merge to arrays
# Actually a bad way because creating an auxiliary array in the function.
def merge(arr1, arr2):
    res = list()
    maxi = len(arr1)
    maxj = len(arr2)
    maxk = maxi + maxj
    i, j, k = 0, 0, 0
    for k in range(0, maxk):
        # case 1
        if i == maxi and j < maxj:
            res.append(arr2[j])
            j += 1
            continue
        # case 2
        if i < maxi and j == maxj:
            res.append(arr1[i])
            i += 1
            continue
        # case 3
        if i < maxi and j < maxj:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
                continue
            else:
                res.append(arr2[j])
                j += 1
                continue
    return res

arr1 = [1,3,5]
arr2 = [6,1,2]

res = merge(arr1, arr2)
print(f'result : {res}')
# %%
import math
import numpy as np
def merge(aux, arr, lo, mid, hi):
    for i in range(lo, hi+1):
        aux[i] = arr[i]
    i = lo
    j = mid+1
    maxi = mid
    maxj = hi
    # k = lo
    # while i <= maxi or j <= maxj:
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
            if aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
                k += 1
                continue
            else:
                arr[k] = aux[j]
                j += 1
                k += 1
                continue

arr = [1,3,5,2,4]
aux = np.zeros(len(arr))
lo = 0
hi = len(arr)-1
mid = math.floor((lo+hi)/2)
print(f'mid {mid}')
aux = merge(aux, arr, lo, mid, hi)
print(f'result : {arr}')