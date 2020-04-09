'''
Problem of the Day:
Given a string S and a character C.

Return an array of integers representing the shortest distance from the character C to each character in the string.

Example:
                      
  Input: S = "helloworld", C = 'o'
  Output: [4, 3, 2, 1, 0, 1, 0, 1, 2, 3]

  Input: S = "bloomberg", C = 'o'
  Output: [2, 1, 0, 0, 1, 2, 3, 4, 5]
                      
'''

def shortest(arr, c):
    idx = []
    res = []
    n = len(arr)
    for i in range(n):
        if arr[i] == c:
            idx.append(i)
    i = 0
    j = 0
    while i < n:
        if i <= idx[j] :
            res.append(abs(idx[j]-i))
            i += 1

        elif len(idx) > j+1:
            while i <= idx[j+1]:
                minimum = min (abs(idx[j+1]-i), abs(idx[j]- i) )
                res.append(minimum)
                i += 1
            j += 1

        elif i > idx[j]:
            res.append(abs(i - idx[j]))
            i += 1

    
    return res

print(shortest("bloomberg", 'o'))