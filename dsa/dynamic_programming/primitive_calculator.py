# Naive recurrsive solution
opt_list = []
def operate(num):
    opt_list.append(num)
    if num == 0:
        # print('+ 1')
        for i in range(len(opt_list)-1, -1, -1):
            # print(i)
            print(opt_list[i])
        print('Opts: ', len(opt_list)-1)
        return
    if num % 3 == 0:
        # print('x 3')
        # opt_list.append(num/3)
        operate(num/3)
    elif num % 2 == 0:
        # print('x 2')
        operate(num/2)
    else:
        # print('+ 1')
        operate(num-1)
# operate(96234)


import numpy as np
options = [1, 2, 3]
num = 36
table = np.zeros(shape=(3, num+1))
for i in range(0,3):
    for j in range(1, num+1):
        # print('Curr Num ', j)
        if i == 0:
            table[i][j] = table[i][j-1] + 1
        if i == 1:
            if int(j % 2) == 0:
                table[i][j] = min(table[i-1][j], table[i][j-1] + 1, table[i][int(j/2)] + 1)
            else:
                table[i][j] = table[i][j-1] + 1
        if i == 2:
            if int(j % 3) == 0:
                table[i][j] = min(table[i-1][j], table[i][j-1] + 1, table[i][int(j/3)] + 1)
            else:
                table[i][j] = table[i][j-1] + 1
# print(table[2][num])




print(table)
opt_list = []
i = 2
j = num
while num > 0:
    print('curr num ', num)
    if int(num%3) != 0 and int(num%2) != 0:
        num = num - 1
        opt_list.append('+1')
        continue
    
    if int(num%2) == 0 and int(num%3) != 0:
        if table[2][int(num/2)] + 1 ==  table[2][int(num)]:
            num = int(num/2)
            opt_list.append('*2')
        else:
            num = num - 1
            opt_list.append('+1')
        continue
    
    if int(num%3) == 0 and int(num%2) != 0:
        if table[2][int(num/3)] + 1 ==  table[2][int(num)]:
            num = int(num/3)
            opt_list.append('*3')
        else:
            num = num - 1
            opt_list.append('+1')
        continue
    
    if int(num%2) == 0 and int(num%3) == 0:
        print('In')
        print('table[2][int(num/3)]: ', table[2][int(num/3)], 'table[2][int(num)]: ', table[2][int(num)])
        print('table[2][int(num/2)]: ', table[2][int(num/2)], 'table[2][int(num)]: ', table[2][int(num)])
        print('table[2][int(num-1)]: ', table[2][int(num-1)], 'table[2][int(num)]: ', table[2][int(num)])
        if table[2][int(num/3)] + 1 ==  table[2][int(num)]:
            num = int(num/3)
            opt_list.append('*3')
        elif table[2][int(num/2)] + 1 ==  table[2][int(num)]:
            num = int(num/2)
            opt_list.append('*2')
        a = table[2][int(num/2)] + 1
        b = table[2][int(num/3)] + 1
print(opt_list)
print(len(opt_list))










