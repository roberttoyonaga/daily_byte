class Solution:
    def DFS(self, grid, visited, m , n):
        #stopping conditions
        if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]) or grid[m][n]=="0" or visited[m][n]:
            return
        visited[m][n] = True
        
        self.DFS(grid, visited, m, n+1)
        self.DFS(grid, visited, m, n-1)
        self.DFS(grid, visited, m+1, n)
        self.DFS(grid, visited, m-1, n)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = []
        for i in range(len(grid)):
            visited.append([False]*len(grid[0]))
            
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if not visited[m][n] and grid[m][n]=="1":
                    count += 1
                    self.DFS(grid, visited, m, n)
                    
        return count