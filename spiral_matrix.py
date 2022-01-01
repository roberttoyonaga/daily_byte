class Solution(object):
    def __init__(self):
        self.directions = {"up":(-1,0), "down":(1,0), "right":(0,1), "left":(0,-1)}
        self.next_direction = {"up":"right", "down": "left", "right":"down","left":"up"}
        self.direction = "right"
        self.row = 0
        self.col = 0
        self.matrix = None
        
    def is_valid_element(self, row,col):
        if row >= len(self.matrix) or row < 0:
            return False
        if col >= len(self.matrix[0]) or col < 0:
            return False
        if self.matrix[row][col] > 100:
            return False
        return True
    
        
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # let's mark visited elements with  101 (outside specified range)
        
        self.matrix = matrix
        ret = []
        
        # handle first element
        if self.is_valid_element(self.row,self.col):
            ret.append(self.matrix[self.row][self.col])
            self.matrix[self.row][self.col] = 101 # set to visited
        else:
            return ret
        
        while(True):
            direction_tuple = self.directions[self.direction]
            next_row = self.row + direction_tuple[0]
            next_col =  self.col + direction_tuple[1]
            #can we keep going in the same direction?
            if self.is_valid_element(next_row,next_col):
                self.row = next_row
                self.col = next_col
                ret.append(self.matrix[self.row][self.col])
                self.matrix[self.row][self.col] = 101 # set to visited
                continue
            # try turning
            self.direction = self.next_direction[ self.direction ]
            direction_tuple = self.directions[ self.direction ]
            next_row = self.row + direction_tuple[0]
            next_col =  self.col + direction_tuple[1] 
            if self.is_valid_element(next_row,next_col):
                self.row = next_row
                self.col = next_col
                ret.append(self.matrix[self.row][self.col])
                self.matrix[self.row][self.col] = 101 # set to visited
                continue
            # we've visited all the elements
            return ret
                
      