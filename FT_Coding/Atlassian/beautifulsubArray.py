### Complexity 0(n2)
def beautifulsubArray(a, m):
    count = 0; 
    n = len(a)

    for i in range(n):  
        odd = 0; 
        for j in range(i, n):  
            if (a[j] % 2): 
                odd += 1; 
            if (odd == m): 
                count += 1
    return count
### complexity 0(n)
def beautifulSubarrays(a, m):  
    count = 0
    prefix = [0] * n  
    odd = 0
    n = len(a)
    # traverse in the array  
    for i in range(n): 
        prefix[odd] += 1
  
        # if array element is odd  
        if (a[i] & 1):  
            odd += 1
  
        # when number of odd elements>=M  
        if (odd >= m):  
            count += prefix[odd - m]  
  
    return count

print(beautifulsubArray([1,2,3,4,5], 2))