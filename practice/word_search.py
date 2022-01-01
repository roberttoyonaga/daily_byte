# import copy
# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         for row in range(len(board)):
#             for col in range(len(board[0])):
#                 if board[row][col]==word[0]:
#                     visited = [] # need visited array to prevent reuse of letters
#                     for i in board:
#                         visited.append([False]*len(board[0]))
#                     if self.search(row,col,board,word,0, visited):
#                         return True
#         return False
#     def search(self,row,col,board,word,position, visited):
#         if position==len(word):
#             return True
        
#         #check boundaries
#         if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
#             return False
        
#         if word[position] != board[row][col]:
#             return False
        
#         if visited[row][col]:
#             return False
        
#         visited_copy = copy.deepcopy(visited)
#         visited_copy[row][col] = True
        
#         return self.search( row, col -1,board, word, position+1,visited_copy) or self.search( row - 1, col,board, word, position+1,visited_copy) or self.search(row + 1, col,board, word, position+1,visited_copy) or self.search(row, col + 1,board, word,  position+1,visited_copy) 


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                
                    if self.search(row,col,board,word,0):
                        return True
        return False
    def search(self,row,col,board,word,position):
        if position==len(word):
            return True
        
        #check boundaries
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        if word[position] != board[row][col]:
            return False
        
        if board[row][col] == "#": # reuse the board! Faster than copying whole board
            return False
        
        letter = board[row][col] 
        board[row][col] = "#"
        
        result =  self.search( row, col -1,board, word, position+1) or self.search( row - 1, col,board, word, position+1) or self.search(row + 1, col,board, word, position+1) or self.search(row, col + 1,board, word,  position+1) 
        
        board[row][col] = letter #we always reset after we modify
        return result
