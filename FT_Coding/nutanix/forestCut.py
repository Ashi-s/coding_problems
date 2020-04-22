def treesCut(s):
    n = len(s)
    count  = 0
    if n % 2 == 0:
        if s[n//2] > s[n//2 -1]:
            for i in range(n//2, n):
                if i+1 < n and s[i+1] <  s[i]:
                    continue
                else:
                    count += 1
            for i in range(n//2):
                if i+1 < n//2 and s[i+1] > s[i]:
                    continue
                else:
                    count += 1

    return count 

print(treesCut([1,2,100,99]))

def bitonic(arr, n): 
      
    # Length of increasing subarray ending at all indexes 
    inc = [None] * n  
      
    # Length of decreasing subarray starting at all indexes 
    dec = [None] * n 
      
    # length of increasing sequence ending at first index is 1 
    inc[0] = 1
      
    # length of increasing sequence starting at first index is 1 
    dec[n-1] = 1
  
    # Step 1) Construct increasing sequence array 
    for i in range(n): 
        if arr[i] >= arr[i-1]: 
            inc[i] = inc[i-1] + 1
        else: 
            inc[i] = 1
  
    # Step 2) Construct decreasing sequence array 
    for i in range(n-2,-1,-1): 
        if arr[i] >= arr[i-1]: 
            dec[i] = inc[i-1] + 1
        else: 
            dec[i] = 1
  
    # Step 3) Find the length of maximum length bitonic sequence 
    max = inc[0] + dec[0] - 1
    for i in range(n): 
        if inc[i] + dec[i] - 1 > max: 
            max = inc[i] + dec[i] - 1
  
    return max
  
# Driver program to test above function 
  
arr = [3,17,4,12,5,6,2,1] 
n = len(arr) 
print("nLength of max length Bitnoic Subarray is ",bitonic(arr, n)) 
                     




