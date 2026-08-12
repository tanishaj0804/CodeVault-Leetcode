class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i,j):
            grid[i][j] = 0
            for dr,dc in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=dr<m and 0<=dc<n and grid[dr][dc]:
                    dfs(dr,dc)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i==0 or j==0 or i==m-1 or j==n-1):
                    dfs(i,j)
        return sum(sum(row) for row in grid)
        