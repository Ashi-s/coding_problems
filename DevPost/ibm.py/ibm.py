# move all zero at the start
# def move_zero_to_first_stable(a):
# 	n = len(a)
# 	j = n-1
#     for i in range(n-1, -1, -1):
#         if a[i] is 0:
#             continue
#         a[j] = a[i]

#         j -= 1
#     while j >= 0:
#         a[j] = 0
#         j -= 1
#     return a

#print(move_zero_to_first_stable([0,1,0,1]))

def minSwaps(arr) : 
  
    numberOfOnes = 0
    n = len(arr)
    for i in range(0, n) : 
  
        if (arr[i] == 1) : 
            numberOfOnes = numberOfOnes + 1
      
    x = numberOfOnes 
      
    count_ones = 0
    maxOnes = 0
      
    for i in range(0, x) : 
  
        if(arr[i] == 1) : 
            count_ones = count_ones + 1
          
    maxOnes = count_ones 
          
    
    for i in range(1, (n - x + 1)) : 
          
        if (arr[i - 1] == 1) :  
            count_ones = count_ones - 1
          
        if(arr[i + x - 1] == 1) : 
            count_ones = count_ones + 1
          
        if (maxOnes < count_ones) : 
                maxOnes = count_ones 
      
    numberOfZeroes = x - maxOnes 
      
    return numberOfZeroes 

#print(minSwaps([0,1,0,1]))


def min_swap(arr):
    n = len(arr)
    noOfZeroes = [0] * n 
    count = 0
      

    noOfZeroes[n - 1] = 1 - arr[n - 1] 
    for i in range(n-2, -1, -1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 0) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
  

    for i in range(0, n) : 
        if (arr[i] == 1) : 
            count = count + noOfZeroes[i] 
  
    return count 
print(min_swap([1,1,1,1,0,1,0,1]))

def findMinSwaps(arr) :
    n = len(arr) 
    
    noOfZeroes = [1] * n 
    count1 = 0
      
    noOfZeroes[n - 1] = arr[n - 1] - 0
    for i in range(n-2, -1, -1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 1) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
  
    for i in range(0, n) : 
        if (arr[i] == 0) : 
            count1 = count1 + noOfZeroes[i] 
  
    return count1
print(findMinSwaps([1,0,1,0,0,0,0,1]))

# Final Output
'''
Minimum swap at either be on any side start or end 
thats why two program one takes 1 at start and the other take 1 at the end 
return min of the two output
'''
def min_swap(arr):
    noOfZeroes = [0] * n 
    count = 0
      

    noOfZeroes[n - 1] = 1 - arr[n - 1] 
    for i in range(n-2, -1, -1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 0) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
  

    for i in range(0, n) : 
        if (arr[i] == 1) : 
            count = count + noOfZeroes[i] 
            
    noOfZeroes = [1] * n 
    count1 = 0
      
    noOfZeroes[n - 1] = arr[n - 1] - 0
    for i in range(n-2, -1, -1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 1) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
  
    for i in range(0, n) : 
        if (arr[i] == 0) : 
            count1 = count1 + noOfZeroes[i] 
            
    return min(count, count1)


''' 
My approach: 
1. To move all zeroes to "left" count each zero on right side of 1
    e.g [0, 0, 1, 0, 1, 0, 1, 1] here index(2) has 2 zeroes & index(4) has 1 zero on right
    therefore output = 3
2. To move all ones to "left" count each ones on right side of 0
    e.g [0, 0, 1, 0, 1, 0, 1, 1] here index(0) has 4 ones & index(1) has 4 ones on right
    and index(3) has 3 ones & index(3) has 2 ones on right therefore output = 13
3. return min(3, 12)
    bcoz we need to check both the case & find the min
''' 

def my_approach(s):
    zeroes = []
    ones = []
    for i in range(len(s)):
        if s[i] == 0:
            continue
        else:
            zeroes.append(len(s[i+1:]) - sum(s[i+1:]))
    for i in range(len(s)):
        if s[i] == 1:
            continue
        else:
            ones.append(len(s[i+1:]) - sum(s[i+1:]))
    return min(sum(ones), sum(zeroes))

print('---------MY APPROACH---------')
print(my_approach([0, 0, 1, 0, 1, 0, 1, 1]))



