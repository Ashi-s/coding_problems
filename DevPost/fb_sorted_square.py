'''
Input: a sorted array 
Output: Squared sorted array
O(n) complexity

e.g = [-6,-4,1,2,3,5]
output: [1,4,9,16,25,36]
'''

def sorted_square(s):
    if s == []:
        return "Invalis"
    n = len(s)
    low = 0
    high = n-1
    out = [0]*n
    while n > 0 :
        if abs(s[low]) > abs(s[high]):
            out[n-1] = s[low] * s[low]
            low += 1
        else:
            out[n-1] = s[high] * s[high]
            high -= 1
        n -= 1 
    return out

print(sorted_square([-6,-4,1,2,3,5]))

