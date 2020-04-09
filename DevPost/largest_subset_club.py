'''
input: [1,6,10,4,7,9,5]
output : 4,5,6,7

[1,4,5,6,7,9,10]
'''

def largest_subset(arr):
    ans = 0
    d = {}
    aSet = set(arr)
    for i in range(len(arr)):
        if arr[i] - 1 not in aSet:
            j = arr[i]
            while j in aSet:
                j += 1
            
            d[arr[i]] = j -arr[i]
            ans = max(ans, j-arr[i])
            
    print(d)
    for i in range(ans):
        print(max(d, key=d.get)+i, end = "")
    #print(max(d, key=d.get))
    print('\n')
    return ans


    

print(largest_subset([1,6,10,4,7,9,5]))
#print(largest_subset([1, 9, 3, 10, 4, 20, 2] ))
