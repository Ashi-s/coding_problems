def getMinimumUniqueSum(arr):
    # Write your code here
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    d = dict(sorted(d.items(),key = lambda x: x[0]))
    return d

print(getMinimumUniqueSum([3,2,1,2,7]))