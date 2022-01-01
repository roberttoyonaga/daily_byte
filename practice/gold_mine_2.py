def gold_mine(board):
    max_gold = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                max_gold = max(max_gold, collect_gold(board, i, j))
    return  max_gold

def collect_gold(board, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 0 :
        return 0

    original = board[row][col]
    board[row][col] = 0 #so we know this is visited

    new_gold = 0
    new_gold = max(new_gold, collect_gold(board, row+1, col))
    new_gold = max(new_gold, collect_gold(board, row, col+1))
    new_gold = max(new_gold, collect_gold(board, row-1, col))
    new_gold = max(new_gold, collect_gold(board, row, col-1))

    board[row][col] = original # reset as if we never messed this up
    return new_gold + original # every time we recurse back, we accumulate sum
    

goldMine = [[0,2,0],[8,6,3],[0,9,0]]
print(gold_mine(goldMine))