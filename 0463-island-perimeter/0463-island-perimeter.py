class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        total = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    total += 4
                    if i and grid[i-1][j]:
                        total -= 2
                    if j and grid[i][j-1]:
                        total -= 2
        return total
        