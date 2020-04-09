'''
Input: [False, True, False, True, False, True, False], pto=2
  Output: 5
  Why?
  If we take PTO on indices [2] and [4], 
  then we can get the maximum length vacation (consecutive True's)
'''

def maxVacation(string, pto):
    n = len(string)
    #solution = [0]*n
    maximum = 0

    for i in range(n):
        summed = 0
        m = 0
        p = pto
        for j in range(i, n):
            if string[j] == False and p <= 0:
                summed = 0
                break
            elif string[j] == False and p > 0:
                summed += 1
                m = summed
                p  -= 1
            else:
                summed += 1
                m = summed
        if m > maximum:
            maximum = m
        #solution[i] = m
    #print(solution)
    
    #return max(solution)
    return maximum
print(maxVacation([False, True, False, True, False, True, False], pto=2))

# [-1, -3, 4, 2, -5, 3]
def maxSeq(string):
    summed = 0
    solution = [0]*len(string)
    for i, val in enumerate(string):
        if summed < 0:
            summed = 0
        summed += val
        solution[i] = summed
    print(solution)
    return max(solution)

print(maxSeq([-1, -3, 4, 2, -5, 3]))
print(maxSeq([-2,-3,4, -1,-2,1,5,-3]))

