'''
Given an array of positive and negative integers {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed) 
sort the array in a way such that the starting from a positive number, the elements should be arranged 
as one positive and one negative element maintaining insertion order. 
First element should be starting from positive integer and the resultant array should look like {6,-1,9,-4,8,-10,8,-9,4}

- sameerasusmitha 4 months ago in India | Report Duplicate | Flag
'''
def alternate(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] < 0:
                helper(i, s)
        else:
            if s[i] > 0:
                helper(i, s)

    def helper(index, s):
        if s[i] < 0:
            for i in range(index+1, len(s)):
                if s[i] >0 :
                    s[i], s[index] = s[index], s[i]
        else:
            for i in range(index+1, len(s)):
                if s[i] < 0:
                    s[i], s[index] = s[index], s[i]
    return s

print(alternate([6,-1,9,-4,8,-10,8,-9,4]))
        


