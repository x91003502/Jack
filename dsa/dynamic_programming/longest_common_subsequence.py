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
    # print(table)
    return result
    # result = []
    # on_steps = table[len(s2)][len(s1)]
    # j = len(s2)
    # i = len(s1)
    # while on_steps > 0:
    #     if i == 0 and j == 0: return
    #     curr = table[j][i]
    #     print(f'from table[{j}][{i}]')
    #     if i > 0 and curr == table[j][i-1] + 1:
    #         i -= 1
    #         on_steps -= 1
    #         continue
    #     elif j > 0 and curr == table[j-1][i] + 1:
    #         j -= 1
    #         on_steps -= 1
    #         continue
    #     else:
    #         if table[j][i] != table[j-1][i-1]:
    #             on_steps -= 1
    #         else:
    #             print(f'Match. s1[{i}] = s2[{j}]')
    #             result.append(s1[i-1])
    #         i -= 1
    #         j -= 1
    # return result
s1 = '132'
s2 = '123'
s3 = '135'
s4 = '125'
# print(two_string_comparison(s1, s2))
n_strings = [s1, s2, s3, s4]
def n_strings_comparison(n_strings):
    n = len(n_strings)
    if n < 2:
        return n_strings
    if n == 2:
        return two_string_comparison(n_strings[0], n_strings[1])
    if n > 2:
        result = two_string_comparison(n_strings[0], n_strings[1])
        for i in range(2, n):
            result = two_string_comparison(result, n_strings[i])
        return result

print(n_strings_comparison(n_strings))