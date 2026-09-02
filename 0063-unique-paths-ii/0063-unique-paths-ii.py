class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0
        for i in range(m):
            if grid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if grid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

        