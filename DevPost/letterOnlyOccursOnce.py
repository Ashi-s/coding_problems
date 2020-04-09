'''
Input: "eeeeffff"
  Output: 1
  Why? We can delete one occurence of e or one occurence of 'f'. 
        Then one letter will occur four times and the other three times.

  Input: "aabbffddeaee"
  Output:  6
  Why: 
  For example, we can delete all occurences of 'e' and 'f' 
  and one occurence of 'd' to obtain the word "aabbda".
  Note that both 'e' and 'f' will occur zero times in the new word, 
  but that's fine, since we only care about the letter
  that appear at least once.

  Input: "llll"
  Output: 0
  Why? There is no need to delete any character.

'''
def occursOnlyOnce(string):
    d = {}
    l = []
    count = 0
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    if len(d) == 1:
        return 0
    aSet = set(d.values())
    print(aSet)
    for key in d:
        if d[key] in aSet:
            print(d[key], aSet)
            aSet.remove(d[key])
            l.append(d[key])
            #print('l -----', l)
        else:
            j = d[key]
            while j >= 0:
                if j-1 not in aSet and j-1 not in l:
                    count += 1
                    if j-1 != 0:
                        aSet.add(j-1)
                        #l.append(j-1)
                    break
                else:
                    j -= 1
                    count += 1
        print('====', aSet,"li ----", l)
    print(d, aSet)
    return count 

    #print(d,val)

print(occursOnlyOnce('aabbffddeaee'))