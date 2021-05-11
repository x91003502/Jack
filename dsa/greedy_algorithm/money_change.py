def money_change(money, coins):
    l = list()
    cmin = min(coins)
    while money >= cmin:
        c = coins[0]
        for i in range(1, len(coins)):
            if money >= coins[i]:
                c= coins[i]
        l.append(c)
        money -= c
    return money, l

money = 28
coins = [2,5,10]
money, l = money_change(money, coins)
print(f'remaining : {money}$. combination " {l}')