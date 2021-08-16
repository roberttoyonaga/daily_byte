'''Given a 2D board that represents a word search puzzle and a string word,
 return whether or the given word can be formed in the puzzle by only connecting
  cells horizontally and vertically.'''
  
def word_search(board, word):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0] and search(board, word,row, col, 0):
                return True
    return False

def search(board, word, row, col, count):
    if count == len(word):
        return True
    
    
    #check boundaries
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    
    #check current letter
    if board[row][col] != word[count]:
        return False

    return search(board, word, row, col -1, count+1) or search(board, word, row - 1, col, count+1) or search(board, word, row + 1, col, count+1) or search(board, word, row, col + 1, count+1) 

board = [ ['C','A','T','F'], ['B','G','E','S'], ['I','T','A','E'] ]
print(word_search(board,"SEAT"))
print(word_search(board,"CACACA"))
