'''
 A ball is dropped into a special Galton board where at each level in the board the ball can
  only move right or down. Given that the Galton board has M rows and N columns, 
  return the total number of unique ways the ball can arrive at the bottom right cell of the Galton board.

  [m][n]  = [m-1][n] + [m][n-1] this solution is M*N time and M*N space
'''
def galton_board(m ,n ):
    board = []
    # this is the way to make a 2d list where each row points to a differnet list 
    #(not all referencing the same list)
    for row in range(m):  
        board.append([0]*n)
    util(board,m,n)

    return board[m-1][n-1]
def util(board,m,n):
    for row in range(m):
        for col in range(n):
            if row==0:
                board[row][col] = 1
            elif col==0:
                board[row][col] = board[row-1][col]
            else:
                board[row][col] = board[row-1][col] + board[row][col-1]

        # debug
        for r in board:
            print(r)
        print("-----")

print(galton_board(4,3))
