def test(mapping, nums):
    my_mapping = {}
    count = 0
    for val in mapping:
        my_mapping[val] = str(count)
        count += 1
    print(mapping)
    shuffled = []
    for num in nums:
        changed = []
        for char in num:
            changed.append(my_mapping[int(char)])
        shuffled.append("".join(changed))

    new_shuffeled = sorted(shuffled, key= lambda x: int(x))
    res = [nums[shuffled.index(val)] for val in new_shuffeled]
    return res