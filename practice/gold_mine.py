'''. Given a 2D matrix that represents a gold mine, where each cell’s value represents an amount of gold, return the maximum amount of gold you can collect given the following rules:

    You may start and stop collecting gold from any position
    You can never visit a cell that contains 0 gold
    You cannot visit the same cell more than once
    From the current cell, you may walk one cell to the left, right, up, or down
'''
import numpy as np
 
def gold_mine(board):
    sums = []
    
    #try starting DFS at each different node in the graph
    for row in range(len(board)):
        for col in range(len(board[row])):
            visited = np.zeros((len(board),len(board[0])))
            search(board, sums,row, col,visited,0)
    return max(sums)


def search(board, sums, row, col, visited,current_sum):
    #stopping condition
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col]==1 or board[row][col]==0:
        sums.append(current_sum)    
        return

    #process current node
    current_sum += board[row][col]
    visited[row][col] = 1

    #recurse 
    search(board, sums, row, col -1, visited, current_sum)
    search(board, sums, row - 1, col, visited, current_sum)
    search(board, sums, row + 1, col, visited, current_sum)
    search(board, sums, row, col + 1, visited, current_sum) 

goldMine = [[0,2,0],[8,6,3],[0,9,0]]
print(gold_mine(goldMine))
