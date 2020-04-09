
user_songs_1 = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}

song_genres_1 = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}
output_1 = {
    "David": ["Rock", "Techno"],
    "Emma":  ["Pop"]
}
def favogenere(user_songs_1,song_genres_1):
    res = {}
    for key in user_songs_1:
        res[key] = []

    for key, value in user_songs_1.items():
        #print('1------', key, value)
        d = {}
        for each in value:
            k = findKey(each)
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
        #print('d ---', d)
        max1 = max(d.values())
        #print('max: ',max1)
        for q,w in d.items():
            if w == max1:
                res[key].append(q)
        # print('d:---', d)
        # print('max---',max(d, key = d.get))
    return res

def findKey(string):
    for key in song_genres_1:
        for each in song_genres_1[key]:
            if each == string:
                return key

print(favogenere(user_songs_1,song_genres_1))



# def favGenere(user_songs, song_genere):
#     d = {}
#     for key, value in user_songs.items():
#         for each in value:
#             for gen in song_genere:
#                 if each in song_genere[gen]:
#                     del user_songs[key][user_songs[key].index(each)]
#                     user_songs[key].append(gen)
    
#     return user_songs

#print(favGenere(user_songs_1, song_genres_1))


