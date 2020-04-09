def solver(amt, coins, i):
    if i>=len(coins):
        return -1
    if amt == 0:
        return 0
    if amt<coins[i]:
        return solver(amt, coins, i+1)
    else:
        return min(1+solver(amt-coins[i], coins, i), solver(amt, coins, i+1))
    

def min_coin(amt, coins):
    
    #coins.sort(reverse=True)
    i=0
    return solver(amt,coins,i)

print(min_coin(53, [50,8,21]))