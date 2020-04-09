def solver(amt, coins, i, d):
    if amt in d:
        return d[amt]
    if i>=len(coins):
        return float('inf')
    if amt == 0:
        return 0
    if amt<coins[i]:
        return solver(amt, coins, i+1, d)
    else:
        res = min(1+solver(amt-coins[i], coins, i, d), solver(amt, coins, i+1, d))
        d[amt] = res
        return res

def min_coin(amt, coins):
    
    coins.sort(reverse=True)
    i=0
    d = {}
    solver(amt,coins,i, d)
    return d[amt]

print(min_coin(63, [1,8,21,50]))