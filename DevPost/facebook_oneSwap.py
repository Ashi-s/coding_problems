'''
input - 2736
output - 7236
maximum value in one swap
'''

def oneSwap(a):
    a = [i for i in str(a)]
    ann = str(a)
    ann = [*enumerate(a)]
    ann.sort(key = lambda x: x[1],reverse = True)
    
    
    #ann.sort(key = lambda x:x[1])

    for i in range(len(ann)):
        if ann[i][0] != i:
            a[i], a[ann[i][0]] = a[ann[i][0]] , a[i]
            break



    return a

print(oneSwap(7000199999))