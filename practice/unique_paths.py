# class Solution:
#     def __init__(self):
#         self.paths = 0
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.util(m-1,n-1) # subtract one from each dimension because we start ON the board
#         return self.paths
#     def util(self, m,n):
#         if m == 0 and n ==0:
#             self.paths +=1
#             return
#         elif m<0 or n<0:
#             return
#         self.util(m-1,n)
#         self.util(m,n-1)
# backtracking solution is too slow  (Exponential run time)

#try a dynamic programming solution  MxN
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = []
        for row in range(m):
            board.append([0]*n)
            
        for col in range(n):
            for row in range(m):
                if row > 0 and col > 0:
                    board[row][col] = board[row-1][col]+board[row][col-1]
                elif row > 0 and col == 0:
                    board[row][col] = board[row-1][col]
                elif row == 0 and col > 0:
                    board[row][col] = board[row][col-1]
                else:
                    board[row][col] = 1
        return board[m-1][n-1]
                    
   