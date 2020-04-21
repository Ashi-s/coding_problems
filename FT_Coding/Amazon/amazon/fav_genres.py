def favGenres(userSongs, songGenres):
    output = {}
    for user in userSongs:
        song_list = userSongs[user]
        count = {}

        for song in song_list:
            for genre in songGenres:
                if(genre not in count):
                    count[genre] = 0
                if(song in songGenres[genre]):
                    count[genre] += 1

        output[user] = [key for key, val in count.items() if val == max(count.values())]

    return output
