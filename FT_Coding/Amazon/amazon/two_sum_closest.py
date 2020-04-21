import sys
def IDsOfSongs(songDurations, rideDuration):
    rd_with_limit = rideDuration - 30
    sorted_sd = sorted(songDurations)
    start = 0
    end = len(songDurations) - 1
    result = sys.maxint
    result_array = None
    while start < end:
        combined_song_duration = sorted_sd[start] + sorted_sd[end]
        if combined_song_duration == rd_with_limit:
            return find_result(songDurations, [sorted_sd[start], sorted_sd[end]])
        elif combined_song_duration > rd_with_limit:
            if abs(combined_song_duration - rd_with_limit) < result:
                result = abs(combined_song_duration - rd_with_limit)
                result_array = [sorted_sd[start], sorted_sd[end]]
            end -= 1
        else:
            if abs(combined_song_duration - rd_with_limit) < result:
                result = abs(combined_song_duration - rd_with_limit)
                result_array = [sorted_sd[start], sorted_sd[end]]
            start += 1
    return find_result(songDurations, result_array)
#
def find_result(songDurations, result_array):
    result_indexes = []
    for x in result_array:
        index = songDurations.index(x)
        songDurations[index] = None
        result_indexes.append(index)

    return result_indexes


sar = [1,2, 3]
ar = [1,3, 2]

0,1

1,2
