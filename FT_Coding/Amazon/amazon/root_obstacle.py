class Point:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


def remove_obstacle(rows, columns, lot):
    queue = []
    d_x = None
    d_y = None
    visited = [[False for i in range(columns)] for j in range(rows)]
    queue.append(Point(0,0,0))
    for i in range(rows):
        for j in range(columns):
            if(lot[i][j] == 0):
                visited[i][j] = True
            else:
                visited[i][j] = False
                if(lot[i][j] == 9):
                    d_x = i;
                    d_y = j;


    while(len(queue) != 0):
        ele = queue.pop(0)
        if(ele.x == d_x and ele.y == d_y):
            return ele.dist

        top_valid = check_if_valid(ele.x-1, ele.y, rows, columns)
        down_valid = check_if_valid(ele.x+1, ele.y, rows, columns)
        left_valid = check_if_valid(ele.x, ele.y-1, rows, columns)
        right_valid = check_if_valid(ele.x, ele.y+1, rows, columns)

        if top_valid and not visited[ele.x-1][ele.y]:
            queue.append(Point(ele.x-1, ele.y, ele.dist+1));

        if(down_valid and not visited[ele.x+1][ele.y]):
            queue.append(Point(ele.x+1, ele.y, ele.dist+1));

        if(left_valid and not visited[ele.x][ele.y-1]):
            queue.append(Point(ele.x, ele.y-1, ele.dist+1));

        if(right_valid and not visited[ele.x][ele.y+1]):
            queue.append(Point(ele.x, ele.y+1, ele.dist+1));

    return -1


def check_if_valid(i, j, rows, columns):
    if(i >= 0 and i < rows and j >= 0 and j < columns):
        return True
    return False



input_array = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 9, 1]
]

input_array_2 = [
    [1, 1, 1],
    [1, 0, 9],
    [1, 1, 1]
]

print(remove_obstacle(5, 4, input_array))
print(remove_obstacle(3, 3, input_array_2))
