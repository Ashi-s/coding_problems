import math
def power(model):
    l = len(model)
    count = 0
    g = 0
    d= {}
    for i in model:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ceiling = int(math.ceil(l/2))
    ds = sorted(d.items(), key=lambda x: x[1], reverse =True)
    for i in ds:
        if i[1]< ceiling and count < ceiling:
            count += i[1]
            g += 1
        else:
            break
    return g

print(power([3,4,6,11,9,9,9,9,8,8,8,8,8,8]))


