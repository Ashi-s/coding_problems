
def evaluate(res):
    stack = []
    if len(res) == 0:
        return 0
    for val in res:
        if val.isalnum():
            stack.append(int(val))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            temp = 0
            if val == '*':
                temp = val2 * val1
            elif val == '/':
                temp = val2 // val1
            elif val == '+':
                temp = val2 + val1
            else:
                temp = val2 - val1
            stack.append(temp)
    #print('##########',stack)
    return stack[-1]


def infix_to_postfix(string):
    d = {'*': 2, '/':2, '+':1, '-':1}
    #prev_cahr = ""
    stack = []
    operand_s = []
    res = []
    i = 0
    for i,val in enumerate(string):
        #print("val: ",val)
        if val == " ":
            continue
        if val.isalnum():
            if len(operand_s) > 0 :
                temp = int(operand_s.pop())
                temp = temp*10
                temp += int(val)
                operand_s.append(str(temp))
            else:
                operand_s.append(val)

            if i == len(string)-1 or not string[i+1].isalnum():
                res.append(str(operand_s.pop()))
        else:
            
            if len(stack) == 0 or d[val] > d[stack[-1]]:
                #print("d[val]:{} d[stack[-1]]: {}".format(d[val],d[stack[-1]]))
                stack.append(val)
            else:
                while len(stack) > 0 and d[stack[-1]] >= d[val]:
                    res.append(stack.pop(-1))
                stack.append(val)
    
    #print("after while")
    #print(stack)
    while len(stack) > 0:
        res.append(stack.pop(-1))
    #print(res)
    return evaluate(res)

# print(infix_to_postfix("13+5 * 2 "))
# print(infix_to_postfix(" 15-4/2"))
# print(infix_to_postfix("   24/2-   10/5   "))
        
def in_to_postfix(string):
    string1 = ""
    for i in string:
        if i != " ":
            string1 += i
    d = {'*': 2, '/':2, '+':1, '-':1}
    stack = []
    res = []
    n = len(string1)
    i = 0

    prev = ""
    while i < n :
        
        if string1[i] == " ":
            i += 1
            print('1---')

        if string1[i].isalnum():
            prev = ""
            while i < n and string1[i].isalnum():
                prev += string1[i]
                i += 1
            res.append(prev)
        else:
            if len(stack) == 0 or d[string1[i]] >= d[stack[-1]]:
                stack.append(string1[i])
                print('-------',stack)
            else:
                while len(stack) > 0 and d[stack[-1]] >= d[string1[i]]:
                    res.append(stack.pop())
                stack.append(string[i])

            i += 1
    while len(stack) > 0:
        res.append(stack.pop())
    
    print('result: ', res)
    return evaluate(res)

        

print(in_to_postfix("13+5 * 2"))
print(in_to_postfix(" 15-4/2"))
    
print(in_to_postfix(" 24/2-10/5 "))

            
            
