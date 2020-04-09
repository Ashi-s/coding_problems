class TicTacToe:
    
    

    def add_element(self,ele, index_x,index_y,board) :
        if index_y != 2:
            board[index_x][index_y] = ele + '|'
        else:
            board[index_x][index_y] = ele + '|'

    def print_the_board(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[ij[j] == 0:
                    print('-')
                # if j != 2:
                    print(board[i][j], "|" , end =" ")
                # else:
                #     print(j , end =" ")
            print('\n')

board = [ [0,0,0 ], [0,0,0], [0,0,0]]
c = TicTacToe()
c.print_the_board(board)
c.add_element('X', 0,0,board)
c.add_element('0', 1,1,board)
c.add_element('X', 1,2,board)   

c.print_the_board(board)


    