import numpy as np

def two_string_comparison(s1, s2):
    table = np.zeros(shape=(len(s2)+1,len(s1)+1))
    for i in range(len(s1)+1):
        table[0][i] = i
    for j in range(len(s2)+1):
        table[j][0] = j
    
    result = []
    for i in range(1, len(s1)+1):
        # print(table[0][i])
        for j in range(1, len(s2)+1):
            insertion = table[j-1][i] + 1
            deletion = table[j][i-1] + 1
            if s1[i-1] == s2[j-1]:
                # print(f'Match. s1[{i}] = s2[{j}]')
                match_or_miss = table[j-1][i-1]
                result.append(s1[i-1])
            else:
                match_or_miss = table[j-1][i-1] + 1
            table[j][i] = min(insertion, deletion, match_or_miss)
    return table

def reconstruct(i, j):
    if i == 0 and j == 0:
        return
    if i > 0 and table[j][i] == table[j][i-1]+1:
        reconstruct(i-1, j)
    elif j > 0 and table[j][i] == table[j-1][i]+1:
        reconstruct(i, j-1)
    else:
        reconstruct(i-1, j-1)
        # print(f'Miss or Match. s1[{i}]= = s2[{j}]')


s1 = '123'
s2 = '345'
s3 = '135'
s4 = '125'
table = two_string_comparison(s3, s4)
j = len(s2)
i = len(s1)
reconstruct(i, j)