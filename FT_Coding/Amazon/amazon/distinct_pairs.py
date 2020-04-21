def countPairs(numCount, ratingValues, target):
    hash_map = {}
    for value in ratingValues:
        if value not in hash_map.keys():
            hash_map[value] = 0
        hash_map[value] += 1

    count = 0
    for value in ratingValues:
        if target-value in hash_map.keys():
            count += hash_map[target-value]

        if(target-value == value):
            count -= 1

    return count/ 2
