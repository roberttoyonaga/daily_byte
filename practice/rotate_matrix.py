class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        '''
        To do this we first get the transpose. Then we mirror the matrix across its vertical axis.
        Figure this out by trying random stuff
        '''
        
        #first get the transpose
        n = len(matrix)
        for row in range(n):
            for column in range(row): # go up to the diagonal
                temp = matrix[column][row]
                matrix[column][row] = matrix[row][column]
                matrix[row][column] = temp
                
        #then mirror the transpose
        for column in range(n//2):
            for row in range(n):
                temp = matrix[row][-column-1]
                matrix[row][-column-1] = matrix[row][column]
                matrix[row][column] = temp
        return matrix