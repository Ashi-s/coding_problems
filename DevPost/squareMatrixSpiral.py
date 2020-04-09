'''
Input: 3
Output: [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
]

Description: Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
'''

def matrixSpiral(input):
    pass

## next question matrix given print in spiral order
'''
Input: [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

'''
def printSpiral(matrix):
    res = []
    if len(matrix) == 1:
        return matrix[0]
    while len(matrix) > 1:
        res += matrix[0]
        del matrix[0]
        #transpose of a matrix
        matrix = list(map(list, zip(*matrix)))
        matrix.reverse()
    
    return res

print(printSpiral([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))

def test(a):
    #a = list(map(list, zip(*a)))
    a = a.reverse()
    print(a)

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(test(a))