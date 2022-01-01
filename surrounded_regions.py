import copy
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        BFS/dfs from each O on the edges, marking visited squares with  'P'. After all Os on the edge         have been visited, then turn all Os to X and all Ps to O.
        
        O(mn)
        
        """
        # find all O's on the outer border and run dfs
        for col in range(len(board[0])):
            if board[0][col] == "O":
                self.dfs(board,0, col)
            if board[-1][col] == "O":
                self.dfs(board,len(board)-1,col)
        for row in range(len(board)):
            if board[row][0] == "O":
                self.dfs(board,row, 0)
            if board[row][-1] == "O":
                self.dfs(board,row,len(board[0])-1)  
            
        # finalize the markers for each spot
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "P":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        
    def dfs(self, board, row,col):
        #are we out of bounds
        if row < 0 or col < 0:
            return
        elif row >= len(board) or col >= len(board[0]):
            return
        elif board[row][col]=="P" or board[row][col]=="X":
            return 
        board[row][col] = "P"
        self.dfs(board, row+1, col)
        self.dfs(board, row, col+1)
        self.dfs(board, row-1, col)
        self.dfs(board, row, col-1)