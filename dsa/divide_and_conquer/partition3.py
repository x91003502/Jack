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

# arr = [6,4,6,2,9,2,5,3,4]
# j, k = partition3(arr, 0, len(arr)-1)
# print(arr)

def quicksort3(arr, lo, hi):
    if hi > lo:
        m1, m2 = partition3(arr, lo, hi)
        quicksort3(arr, lo, m1-1)
        quicksort3(arr, m2+1, hi)

arr = [6,4,6,2,9,2,5]
quicksort3(arr, 0, len(arr)-1)
print(arr)