import numpy as np
num_list = [1, 2, 3]
dictionary = dict()
def RecursiveSum(currIndex, sum, partition):
    for i in range(currIndex+1, len(num_list)):
        new_partition = partition.copy()
        new_sum = sum + num_list[i]
        new_partition.append(i)
        print(f'Add {i}_th number. new_sum : {new_sum}')
        print(new_partition)
        RecursiveSum(i, new_sum, new_partition)

for i in range(0, len(num_list)):
    sum = num_list[i]
    partition = []
    partition.append(i)
    dictionary.update({f'{partition}': i})
    print(f'Start {i}_th number. start_sum : {sum}')
    print(partition)
    RecursiveSum(i, sum, partition)


print(dictionary)



# 3-sum
# for i in range(0, len(num_list)):
#     for j in range(i+1, len(num_list)):
#         for k in range(j+1, len(num_list)):
#             sum = num_list[i] + num_list[j] + num_list[k]
#             print(f'{i}_th + {j}_th + {k}_th = {sum}')