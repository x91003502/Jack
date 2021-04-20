import numpy as np
money = 16
coins = [1, 3, 4]

def change(money, coins):
    table = np.zeros(shape=(len(coins)+1, money+1))
    for m in range(0, money+1):
        table[0][m] = m
    for i in range(1, len(coins)+1):
        print('coin : ', coins[i-1])
        for m in range(1, money+1):
            print('m : ', m)
            table[i][m] = table[i-1][m]
            val = table[i][m-coins[i-1]] + 1
            if m >= coins[i-1]:
                if val < table[i][m]:
                    print('val : ', val, 'table[i][m] : ', table[i][m])
                    table[i][m] = val
    
    i = len(coins)
    j = money
    # print(curr)
    while j > 0:
        # print('left : ', j)
        curr = table[i][j]
        for k in range(i-1, -1, -1):
            # print(k)
            c = coins[k]
            # print('coin : ', c)
            if curr == table[i][j-c] + 1:
                print('has : ', c)
                curr = table[i][j-c]
                j = j - c


    print(table)
    

change(money, coins)
