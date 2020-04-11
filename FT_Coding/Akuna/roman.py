def roman(l):
    d = {}
    for i in d:
        n, r = i.split(" ")
        d[n] = r
    ds = sorted(d.items(), key=lambda x: x[0], reverse =True)
    romanToInt(ds)
    def value(r): 
        if (r == 'I'): 
            return 1
        if (r == 'V'): 
            return 5
        if (r == 'X'): 
            return 10
        if (r == 'L'): 
            return 50
        if (r == 'C'): 
            return 100
        if (r == 'D'): 
            return 500
        if (r == 'M'): 
            return 1000
        return -1
    
    def converts(str): 
        res = 0
        i = 0
    
        while (i < len(str)): 
            s1 = value(str[i]) 
    
            if (i+1 < len(str)): 
                s2 = value(str[i+1]) 
    
                if (s1 >= s2): 
    
                
                    res = res + s1 
                    i = i + 1
                else: 
                    res = res + s2 - s1 
                    i = i + 2
            else: 
                res = res + s
                i = i + 1
    
        return res

    

    def romanToInt(ds):
        for i in ds:
            n = converts(i[1])
            i[1] = n
    return ds


print(roman(["a IX", "a V", "z IV", "t II"]))