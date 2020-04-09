def sudoku2(grid):
    rows = [set() for i in range(9)]
    cols = [set() for j in range(9)]
    sub_mat = [[set() for i in range(3)] for j in range(3)]

    for i in range(9):
        for j in range(9):
            if grid[i][j] != '.':
                if any([grid[i][j] in rows[i], grid[i][j] in cols[j], grid[i][j] in sub_mat[i//3][j//3]]):
                    return False
            
            rows[i].add(grid[i][j])
            cols[j].add(grid[i][j])
            sub_mat[i//3][j//3].add(grid[i][j])
    return True

board = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

print(sudoku2(board))