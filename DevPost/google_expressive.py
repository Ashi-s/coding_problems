'''
Given an original word and an expressive word.

Return the starting and ending index of repeating characters which are not present in original string.

For example, given an original word "Hello" and an expressive word "Heeeellooo". "e" is being repeated 
three times and "o" is being repeated two times so you have to return [["e", 2, 4], ["o", 8, 9]]

Input: original="Hello", expressiveWord = "Heeeellooo"
Output: [["e", 2, 4], ["o", 8, 9]]
Why? "e" is being repeated three times and 
    "o" is being repeated two times.
'''
def expressive_Word(orig, expr):
    res = []
    d_org = {}
    for each in orig:
        if each not in d_org:
            d_org[each] = 1
        else:
            d_org[each] += 1
    d_expr = {}
    for each in expr:
        if each not in d_expr:
            d_expr[each] = 1
        else:
            d_expr[each] += 1

    for i, j in zip(d_org.items(), d_expr.items()):
        if i[1] == j[1]:
            continue
        else:
            res.append([i[0], expr.index(j[0])+1, expr.index(j[0])+j[1]-1])
            
    return res

    
orig= "Ashuus"
expr = "Asssshhhhuusss"
print(expressive_Word(orig, expr))
