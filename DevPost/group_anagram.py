'''
https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
Input: ["eat", "tea", "tan", "ate", "ate", "nat", "bat"]

Output: [
    ["ate", "eat", "tea"]
    ["nat", "tan"]
    ["bat"]
]

Sequence of the Outpput doesn't matter
'''
from collections import defaultdict  
def group_anagram(s):
    d = {}
    res = []
    for i in range(len(s)):
        if s[i][-1] not in d:
            d[s[i][-1]] = [s[i]]
        else:
            d[s[i][-1]].append(s[i])
    print(d)

    for i in range(len(s)):
        if s[i][0] in d:
            print('=---------=', d[s[i][0]][0])
            if d[s[i][0]][0] not in res:
                res.append(d[s[i][0]][0])
                print('lengggggth:', len(d[s[i][0]]))
                if len(d[s[i][0]]) == 1:
                    
                    print('------------------',d[s[i][0]])
                    del d[s[i][0]]
                    print('new---d:  ', d)
                else:
                    d[s[i][0]].pop(0)
            if s[i] not in res:
                res.append(s[i])
                if len(d[s[i][-1]]) == 1:
                    del d[s[i][-1]]
                else:
                    del d[s[i][-1]][0]

    return res, d

Input = ["eat", "tea", "tan", "ate", "nat", "bat"]

#print(group_anagram(Input))


  
def printAnagramsTogether(words): 
    #groupedWords = defaultdict(list) 
    g = {}
  
    # Put all anagram words together in a dictionary  
    # where key is sorted word 
    for word in words: 
        # groupedWords["".join(sorted(word))].append(word) 
        # print(word, groupedWords)
        if ''.join(sorted(word)) not in g:
            g[''.join(sorted(word))] = [word]
        else:
            g[''.join(sorted(word))].append(word)
  
    # Print all anagrams together 
    # for group in groupedWords.values(): 
    #     print(" ".join(group))       

    # for value in g.values():
    #     print(value)
    return list(g.values())

  
  
arr =  ["cat", "dog", "tac", "god", "act"]   
print(printAnagramsTogether(Input)) 