import math
def isPrime(n):
  for i in range (2,int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True

def primeString(string):
    res = []
    for i in string:
        ascii = ord(i)
        if isPrime(ascii):
            res.append(i)
        else:
            s = True
            j = ascii
            k = ascii
            while s:
                if isPrime(j-1) and j-1 >= 65:
                    res.append(chr(j-1))
                    s = False

                elif isPrime(k+1) and k+1 <= 122:
                    res.append(chr(k+1))
                    s = False
                j -= 1
                k += 1
    return ''.join(res)

print(primeString('zex'))

# print([ord(c) for c in 'asdkbjhiUHIOubdaiwudblASjhdblIQ'])
# print([ord(c) for c in primeString('asdkbjhiUHIOubdaiwudblASjhdblIQ')])