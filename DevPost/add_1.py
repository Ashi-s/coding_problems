'''


Problem of the Day:
Given a non-empty array of digits representing a non-negative integer and each element in the array contain a single digit.

Add one (1) to this integer and return it as array.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Note: Converting to the integer and back to the array is not allowed.

Example:
                      
  Input: [3,2,1]
  Output: [3,2,2]

  Input:[9,9,9]
  Output: [1,0,0,0]

  Input:[5,6,9]
  Output: [5,7,0]
'''
def add_1(s):
    carry = 0
    for i in range(len(s)-1, -1,-1):

        temp = int(s[i])

        if i == len(s)-1:
            print(i, len(s))
            temp = int(s[i]) + 1
        temp = temp + carry
        if temp > 9:
            s[i] = str(temp)[1]
            carry = 1
        else:
            s[i] = str(int(temp) + carry)
            carry = 0
        
        #at end if we have carry
        if i == 0 and carry == 1:
            s.insert(0, str(carry)) 
    return s
        
        


print(add_1([9,5,9]))