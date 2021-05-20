def partition(arr,lo,hi):
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

# arr = [6,4,8,2,9,3,9,4,7,6,1]
# partition(arr, 0, len(arr)-1)
# print(arr)

def quicksort(arr, lo, hi):
    if hi > lo:
        m = partition(arr, lo, hi)
        quicksort(arr, lo, m-1)
        quicksort(arr, m+1, hi)


arr = [6,4,8,2,9,3,9,4,7,6,1]
quicksort(arr, 0, len(arr)-1)
print(arr)