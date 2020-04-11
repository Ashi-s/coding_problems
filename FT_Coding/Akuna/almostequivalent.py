# def almost(s,t):
#     if len(s) != len(t):
#         return ["NO"]
#     s_d = {}
#     t_d = {}
#     for i, j in zip(s,t):
#         if i not in s_d:
#             s_d[i] = 1
#         else:
#             s_d[i] += 1
#         if j not in t_d:
#             t_d[j] = 1
#         else:
#             t_d[j] += 1
#     print(s_d, t_d)
    

#     for i in s_d:
#         if i not in t_d:
#             if s_d[i] <= 3:
#                 continue
#             else:
#                 return ["NO"]
#         else:
#             if abs(s_d[i] - t_d[i]) <= 3:
#                 continue
#             else:
#                 return ["NO"]
#     for i in t_d:
#         if i not in s_d and t_d[i] > 3:
#             return ["NO"]
    
#     return ["YES"]




def almost(s,t):
    hash_s = {}
    hash_t = {}

    ## Creating Hashmap for S & T
    for i, j in zip(s,t):
        if i not in hash_s:
            hash_s[i] =1
        else:
            hash_s[i] += 1
        if j not in hash_t:
            hash_t[j] = 1
        else:
            hash_t[j] += 1
    ## Updating hash_t with the sustraction from hash_s 
    ## if any key not in hash_t then append it in hash_t
    for i in hash_s:
        if i in hash_t:
            hash_t[i] = abs(hash_s[i] - hash_t[i])
        else:
            hash_t[i] = hash_s[i]
    ## Comparing if each of Hash_t values are upto 3
    for i in hash_t:
        if hash_t[i] <= 3:
            continue
        else:
            return "NO"
    return "YES"

print(almost('aacccdwwjjj', 'abbbddzzkkk')) 