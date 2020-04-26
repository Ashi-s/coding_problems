## [2,3,2] --> 4
## [4,1,1,4,2] --> 8


def maxSum(arr):
    pick = [0 for i in range(len(arr))]
    dont_pick = [0 for i in range(len(arr))]

    pick[0] = arr[0]

    for i in range(1, len(arr)):
        pick[i] = dont_pick[i-1] + arr[i]
        dont_pick[i] = max(dont_pick[i-1], pick[i-1])

    return max(pick[-1], dont_pick[-1])

print(maxSum([5,1,3,11])) 

## special boundary condition: if first index is included donot include last index in the output
# [5,1,3,11] --output: 12 instead of 16

print(max(maxSum([5,1,3]), maxSum([1,3,11])))

#### writting complete code
## in o(1) space complexity instead of list
def maxSumLooped(arr):
    pick = arr[0]
    dont_pick = 0
    highest = 0
    for i in range(1, len(arr)-1):
        pick , dont_pick = dont_pick + arr[i], max(dont_pick, pick)
    highest = max(pick, dont_pick)

    pick = arr[1]
    dont_pick = 0
    for i in range(2, len(arr)):
        pick , dont_pick = dont_pick + arr[i], max(dont_pick, pick)
        
    return max(highest, pick, dont_pick)

print(maxSumLooped([5,1,3,11]))
