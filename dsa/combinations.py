# A Naive Method For Combinations Generatation.
# To improve: Implement by using iterative method.

# def combination(arr, lst, lo, hi, k):
#     if len(lst) < k:
#         lst.append(arr[lo])
#         print(lst)
#         for i in range(lo+1, hi):
#             combination(arr, lst, i, hi, k)
#         lst.pop()


def combination(arr, lst, lo, hi, k):
    if k > 0:
        lst.append(arr[lo])
        k -= 1
        if k == 0:
            print(k, lst)
        for i in range(lo+1, hi):
            combination(arr, lst, i, hi, k)
        lst.pop()

arr = [1, 2, 3, 4]
lst = list()
for i in range(0, len(arr)):
    combination(arr, lst, i, len(arr), k = 3)