import numpy as np
golds = [1, 4, 8]
W = 10
n_golds = len(golds)

table = np.zeros(shape=(n_golds+1, W+1))
for i in range(0, W+1):
    table[0][i] = i
# print(table)

# for i in range(1, n_golds+1):
#     use_count = 0
#     for w in range(1, W+1):
#         table[i][w] = table[i-1][w]
#         if w >= golds[i-1]:
#             val = table[i][w - golds[i-1]] + 1
#             if val < table[i][w]:
#                 table[i][w] = val
#                 use_count += 1

for i in range(1, 2):
    use_count = 0
    for w in range(1, W+1):
        table[i][w] = table[i][w-1]
        gold = golds[i-1]
        print('gold', gold)
        if w >= golds[i-1] and use_count < 2:
            val = table[i][w - golds[i-1]] + 1
            if val > table[i][w]:
                table[i][w] = val
                use_count += 1

for i in range(2, n_golds+1):
    use_count = 0
    for w in range(1, W+1):
        gold = golds[i-1]
        # print('gold', gold)
        if w >= golds[i-1] and use_count < 1:
            table[i][w] = table[i][w-1]
            val = table[i][w - golds[i-1]] + 1
            if val > table[i][w]:
                table[i][w] = val
                use_count += 1
        else:
            print('w = ', w, ' in else')
            table[i][w] = max(table[i][w-1], table[i-1][w])

j = W
for i in range(n_golds-1, -1, -1):
    if j > 0:
        if table[n_golds][j] == table[n_golds][j-golds[i]] + 1:
            j = j-golds[i]
            print('has : ', golds[i])
            continue