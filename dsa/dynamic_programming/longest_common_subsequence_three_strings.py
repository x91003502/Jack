import numpy as np

def three_string_comparison(s1, s2, s3):
    table = np.zeros(shape=(len(s1)+1, len(s2)+1,len(s3)+1))
    for i in range(len(s1)+1):
        table[i][0][0] = i
    for j in range(len(s2)+1):
        table[0][j][0] = j
    for k in range(len(s3)+1):
        table[0][0][k] = k
    
    result = []
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            for k in range(1, len(s3)+1):
                choice1 = table[i-1][j][k] + 1
                choice2 = table[i][j-1][k] + 1
                choice3 = table[i][j][k-1] + 1
                if s1[i-1] == s2[j-1] and s1[i-1] == s3[k-1]:
                    # print(f'Match. s1[{i}] = s2[{j}]')
                    match_or_miss = table[i-1][j-1][k-1]
                    result.append(s1[i-1])
                else:
                    match_or_miss = table[i-1][j-1][k-1] + 1
                table[i][j][k] = min(choice1, choice2, choice3, match_or_miss)
    print(result)
    return table[i][j][k]

s1 = '83217'
s2 = '8213897'
s3 = '683147'

result = three_string_comparison(s1, s2, s3)
print(result)