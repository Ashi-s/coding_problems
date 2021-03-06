'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def two_sum(s, k):
    for i in s:
        if k - i in s:
            return True
    return False

print(two_sum([10, 15, 3, 7], 17))

