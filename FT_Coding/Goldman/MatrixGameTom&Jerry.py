tomScore = 0
    jerryScore = 0
    ncol = len(board[0])
    maxValuesColumn = []
    for c in range(ncol):
        colmn = [row[c] for row in board]
        maxValuesColumn.append(max(colmn))

    tomturn = True
    maxValuesColumn.sort(reverse=True)

    for i in range(len(maxValuesColumn)):
        if tomturn == True:
            tomScore += maxValuesColumn[i]
            tomturn = False
        else:
            jerryScore += maxValuesColumn[i]
            tomturn = True

    print(abs(tomScore-jerryScore))