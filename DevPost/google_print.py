'''
time (n)
print: if input is 5
5432*
543*1
54*21
5*321
*4321

'''
def print_it(n):
    k = 5
    res = [i for i in range(5,0,-1)]
    for i in range(5,0,-1):
        
        res[k-1] = '*'
        k -= 1
        print(res)



print(print_it(5))
