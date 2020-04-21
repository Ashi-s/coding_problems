'''
Input: "aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.
'''
def substring_k_unique(s, k):
    d = {}
    unique = 0
    n = len(s)
    i = 0
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = [i]
        else:
            d[s[i]].append(i)
    if len(d) < k:
        return "NO Solution"
    

