class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        neg = float('-inf')
        dp = [[neg]*n for _ in range(n)]
        dp[0][0] = grid[0][0]
        for steps in range(1,2*n-1):
            ndp = [[neg]*n for _ in range(n)]
            for r1 in range(n):
                c1 = steps-r1
                if c1<0 or c1>=n:
                    continue
                for r2 in range(n):
                        c2 = steps-r2
                        if c2<0 or c2>=n:
                            continue
                        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                            continue
                        best = neg
                        if r1>0 and r2>0:
                            best = max(best,dp[r1-1][r2-1])
                        if r1>0:
                            best = max(best,dp[r1-1][r2])
                        if r2>0:
                            best = max(best,dp[r1][r2-1])
                        best = max(best,dp[r1][r2])
                        if best == neg:
                            continue
                        if r1 == r2 and c1 == c2:
                            value = grid[r1][c1]
                        else:
                            value = grid[r1][c1]+grid[r2][c2]
                        ndp[r1][r2] = best + value
            dp = ndp
        return max(0,dp[n-1][n-1])
