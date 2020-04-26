## url = https://www.example.com/foo/bar/1
## s = ['/foo', '/foo/bar','/foo/1', '/foo/bar/2'] -- > /foo/bar
'''
def urlMatch(s):
    url = "https://www.example.com/foo/bar/1"
    url_list = ['/'+i for i in url.split('/')[3:]]
    print(url_list)
    url_list_1 = []
    i = 0
    while i < len(url_list):
        url_list_1.append(''.join(url_list[:i+1]))
        i = i+1
    maxlen = ""
    for i in s:
        if i in url_list_1:
            if len(i) > len(maxlen):
                maxlen = i
    if len(maxlen) > 1:
        return maxlen
    else:
        return None
    
'''

def urlMatch1(s):
    url = "https://www.example.com/foo/bar/1"
    spl = url.split('/')[3:]
    print(spl)
    d = {}
    for i in range(len(spl)):
            d[spl[i]] = i
    print(d)

    for i in s:
        sp = i.split('/')[1:]
        
        print(sp)
    

print(urlMatch1(['/foo', '/foo/bar','/foo/1', '/foo/bar/2']))

