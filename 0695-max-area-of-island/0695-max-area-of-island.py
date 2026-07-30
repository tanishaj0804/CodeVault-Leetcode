class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxv = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    c = self.dfs(grid,i,j)
                    maxv = max(maxv,c)
        return maxv
    def dfs(self,grid,i,j):
        count = 0
        if i<0 or i>=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        return (
        1
        + self.dfs(grid, i-1, j)
        + self.dfs(grid, i+1, j)
        + self.dfs(grid, i, j-1)
        + self.dfs(grid, i, j+1)
    )
        