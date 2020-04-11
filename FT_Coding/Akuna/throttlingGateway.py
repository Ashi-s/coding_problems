def droppedRequests(requestTime):
    freq = dict()
    for r in requestTime:
        if r in freq.keys():
            freq[r] = freq[r] + 1
        else:
            freq[r] = 1
    of = sorted(freq.items(), key=lambda x: x[0])
    # print(of)
    dropped = 0
    of2 = dict()
    for k, v in of:
        if v > 3:
            dropped = dropped + v - 3
            of2[k] = 3
        else:
            of2[k] = v
    # print("-single second -")
    x1 = dropped
    # print(dropped)
    # print(of2)

    dropped = 0  ######################

    # run 10 seconds and make of3
    of3 = dict()
    for k in of2.keys():
        start = k
        ten_end = k + 9
        ten_second = 0
        for k2 in of2.keys():
            if start <= k2 <= ten_end:
                ten_second = ten_second + of2[k2]
                if ten_second > 20:
                    x = of2[k2] - (ten_second - 20)
                    if x > 0:
                        of3[k2] = x
                    else:
                        of3[k2] = 0
                else:
                    of3[k2] = of2[k2]
            if k2 > ten_second:
                break
        if ten_second > 20:
            dropped = dropped + ten_second - 20
    y1 = dropped
    # print(of3)

    dropped = 0  ######################

    for k in of3.keys():
        start = k
        minute_end = k + 59
        one_minute = 0
        for k3 in of3.keys():
            if start <= k3 <= minute_end:
                one_minute = one_minute + of3[k3]
            if k3 > minute_end:
                break
        if one_minute > 60:
            dropped = dropped + one_minute - 60
    z1 = dropped
    # print(x1)
    # print(y1)
    # print(z1)
    # print(x1 + y1)
    ans = 0


    if x1 > 0:
        ans += x1
    if y1 > 0:
        ans += x1 + y1
    if z1 > 0:
        ans += z1 + y1+ x1

    # print(ans)

    return ans

print(droppedRequests([1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]))