'''
Given a binary array {0,1,1,0,0,1,0,0,1} , sort the array in a way that 
all zeros come to the left and all the one's come to the right side of the array.

- sameerasusmitha 4 months ago in India | Report Duplicate | Flag |
'''
def left_0_right_1(s):
    ones = sum(s)
    zeroes = len(s) - ones

    return [0]*zeroes + [1]*ones


print(left_0_right_1([0,1,1,0,0,1,0,0,1]))