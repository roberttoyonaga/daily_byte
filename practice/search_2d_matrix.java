class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        /*
        Search 2D matrix 2
        Each element is larger than all the elements to the left and above it.
        O(m+n)
        
        Two pointer method.
        We need to increase one while decreasing the other because if we increase/decrease both, we risk jumping over and skipping our target
        
        */
        int col = 0;
        int row = matrix.length-1;
        int cols = matrix[0].length;
        while (row >= 0 && col < cols) {
            if (matrix[row][col] > target){ // move down if too big
                row--;
            } else if (matrix[row][col] < target) { //move right if too small
                col++;
            } else {
                return true;
            }
        }
        return false;
    }
}