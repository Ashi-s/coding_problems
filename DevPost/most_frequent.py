'''
Input: 
  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
  banned = ["hit"]
  Output: "ball"
  Why? 
  "hit" occurs 3 times, but it is a banned word.
  "ball" occurs twice (and no other word does),
  so it is the most frequent non-banned word in the paragraph. 
  Note that words in the paragraph are not case sensitive,
  that punctuation is ignored (even if adjacent to words, such as "ball,"
'''

def most_frequent(paragraph, banned):
    paragraph = paragraph.lower()
    paragraph = paragraph.replace(',', '')
    paragraph = paragraph.replace('.', '')
    d = {}
    
    for each in paragraph.split(" "):
        if each not in d:
            d[each] = 1
        else:
            d[each] += 1

    d = dict(sorted(d.items(), key = lambda x:x[1], reverse= True))
    print(d)
    for key, value in d.items():
        if key not in banned:
            return key
    return False


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_frequent(paragraph,banned))
