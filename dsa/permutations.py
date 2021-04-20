# A Naive Method For Permutations Generatation.
# To Improve: Creating copy list recursively, space complexity is O(n^2).
def permutation(arr, lst, opt):
    if len(opt) > 0:
        for i in range(0, len(opt)):
            opt_copy = opt.copy()
            opt_copy.remove(opt[i])
            lst_copy = lst.copy()
            lst_copy.append(arr[opt[i]])
            permutation(arr, lst_copy, opt_copy)
    else:
        print('lst : ', lst, ' opt ', opt)


arr = [1, 2, 3]
opt = list()
lst = list()
for i in range(len(arr)):
    opt.append(i)

for i in range(0, len(opt)):
    opt_copy = opt.copy()
    opt_copy.remove(opt[i])
    lst_copy = lst.copy()
    lst_copy.append(arr[opt[i]])
    permutation(arr, lst_copy, opt_copy)