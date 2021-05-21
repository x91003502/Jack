def partition(arr, lo, hi):
    p = arr[lo]
    j = lo
    for i in range(lo+1, hi+1):
        if arr[i] > p: continue
        else:
            j += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[lo]
    arr[lo] = arr[j]
    arr[j] = temp
    return j

def partition3(arr,lo,hi):
    p = arr[lo]
    j = lo
    k = lo
    for i in range(lo+1, hi+1):
        if arr[i] > p: continue
        
        if arr[i] == p:
            k += 1
        else:
            j += 1
            k += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[lo]
    arr[lo] = arr[j]
    arr[j] = temp
    return j, k