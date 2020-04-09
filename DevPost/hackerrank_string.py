# song_genres_1 = {
#     "Rock":    ["song1", "song3"],
#     "Dubstep": ["song7"],
#     "Techno":  ["song2", "song4"],
#     "Pop":     ["song5", "song6"],
#     "Jazz":    ["song8", "song9"]
# }

def hackerString(s):
    d = {}
    string = "hackerrank"
    for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                #print(d[s[i]], d[s[i]].append(i))
                d[s[i]].append(i)
    print(d)
    for i in range(len(string)):
        if string[i] not in d:
            return "NO"
        for j in range(len(d[string[i]])):
            if i <= d[string[i]][j]:
                print('-----', string[i], '----', d[string[i]][0])
                del d[string[i]][j]
                print(d)
                break
            else:
                return "NO"
    return "YES"

def hackerrankMatch(s):
    string = 'hackerrank'
    j = 0
    for i in s:
        if i == string[j]:
            j += 1
        if j == len(string):
            break
    if j == len(string):
        return "YES"
    else:
        return "NO"

# def sortString(s):
#     s.sort()
#     return s

#print(sortString('asdfrgfv'))

print(hackerrankMatch('haccccccccccckerrrrrannnnkkkkkkkk'))

