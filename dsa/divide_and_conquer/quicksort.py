from dsa.divide_and_conquer.partition import partition, partition3

def quicksort(arr, lo, hi):
    if hi > lo:
        m = partition(arr, lo, hi)
        quicksort(arr, lo, m-1)
        quicksort(arr, m+1, hi)

def quicksort3(arr, lo, hi):
    if hi > lo:
        m1, m2 = partition3(arr, lo, hi)
        quicksort3(arr, lo, m1-1)
        quicksort3(arr, m2+1, hi)

def recur_elim_quicksort(arr, lo, hi):
    while hi > lo:
        m = partition(arr, lo, hi)
        print(f'left partition from {lo} to {m-1}  |  right partition from {m+1} to {hi}')
        print(f'run recursive quicksort from {lo} to {m-1}')
        recur_elim_quicksort(arr, lo, m-1)
        lo = m + 1

def recur_elim_quicksort2(arr, lo , hi):
    while hi > lo:
        m = partition(arr, lo, hi)
        n_left = (m-1) - lo + 1
        n_right = (hi) - (m+1) + 1
        print(f'left partition from {lo} to {m-1}  |  right partition from {m+1} to {hi}')
        print(f'{n_left} elements in left partition from  |  {n_right} elements in right partition')
        if n_left <= n_right:
            print('run recursive quicksort on left partition')
            recur_elim_quicksort(arr, lo, m-1)
            lo = m + 1
        else:
            print('run recursive quicksort on right partition')
            recur_elim_quicksort(arr, m+1, hi)
            hi = m - 1