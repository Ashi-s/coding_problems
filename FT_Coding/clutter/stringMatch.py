# def stringMatch(l):
#     li = []
#     for each in l:
#         last = each.split()[-1]
#         for i in l:
#             first = i.split()[0]
#             if last == first:
#                 s = i[len(first):]
#                 li.append(each + s )
#     return li

# #print(stringMatch(['this is Ashish', 'Ashish how r u', 'i am good', 'good is happy', ]))

# print(stringMatch(['mission statement', 'a quick bite to eat', 'a chip off the old block', 'chocolate bar', 'mission impossible', 'a man on a mission', 'block party', 'eat my words', 'bar of soap']))

def stringMatch(l):
    d = {}
    li = []
    for i in l:
        d[i.split()[0]] = l.index(i)
    for i in l:
        if i.split()[-1] in d:
            li.append(i + ' '.join(l[d[i.split()[-1]]].split()[1:]))
    return li
print(stringMatch(['mission statement', 'a quick bite to eat', 'a chip off the old block', 'chocolate bar', 'mission impossible', 'a man on a mission', 'block party', 'eat my words', 'bar of soap']))

#########Using Hashmap to reduce time 
def almost(s,t):
    if len(s) != len(t):
        return ["NO"]
    s_d = {}
    t_d = {}
    for i, j in zip(s,t):
        if i not in s_d:
            s_d[i] = 1
        else:
            s_d[i] += 1
        if j not in zip(t_d):
            t_d[j] = 1
        else:
            t_d[j] += 1
    print(t_d, s_d)
    for i in s_d:
        if i in t_d:
            if abs(s_d[i] - t_d[i]) <= 3:
                continue
            else:
                return ["NO"]
        else:
            if t_d[i] <= 3:
                continue
            else:
                return ["NO"]
    return ["YES"]

print(almost('aacccdwwjjjj', 'abbbddzzkkkk')) 