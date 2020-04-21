def locationOfTargetValue(rowCount, colCount, matrix, targetValue):
    if rowCount == 1:
        return binarySearch(matrix, 0, 0, colCount - 1, targetValue)

    i_low = 0
    i_high = rowCount - 1
    j_mid = colCount // 2

    while((i_low + 1) < i_high):
        i_mid = (i_low + i_high) // 2
        if(matrix[i_mid][j_mid] == targetValue):
            return (i_mid, j_mid)
        elif(matrix[i_mid][j_mid] > targetValue):
            i_high = i_mid
        else:
            i_low = i_mid

    if(matrix[i_low][j_mid] == targetValue):
        return(i_low, j_mid)
    elif(matrix[i_low + 1][j_mid] == targetValue):
        return(i_low + 1, j_mid)
    elif(targetValue >= matrix[i_low][j_mid + 1] and targetValue <= matrix[i_low][colCount - 1]):
        return binarySearch(matrix, i_low, j_mid + 1, colCount - 1, targetValue)
    elif(targetValue <= matrix[i_low + 1][j_mid - 1]):
        return binarySearch(matrix, i_low + 1, 0, j_mid - 1, targetValue)
    else:
        return binarySearch(matrix, i_low + 1, j_mid + 1, colCount - 1, targetValue)


def binarySearch(matrix, i, low, high, targetValue):
    while(low <= high):
        mid = (low + high) // 2
        if(matrix[i][mid] == targetValue):
            return (i, mid)
        elif(matrix[i][mid] > targetValue):
            high = mid - 1
        else:
            low = mid + 1
    return (-1, -1)

input = [
[ -3, 1, 31, 40],
[10, 33, 40, 660],
[123,141,4141,1234],
[22, 43, 161, 702],
[21, 44, 162, 701]
]
# print(locationOfTargetValue(5,4, input, 162))


def locationOfTargetValue(rowCount, colCount, matrix, targetValue):
    for i in range(rowCount):
        for j in range(colCount):
            if matrix[i][j] == targetValue:
                return [i,j]

    return [-1, -1]

print(locationOfTargetValue(5,4, input, 162))
# print search(input, )
