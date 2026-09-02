class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited =set()
        sr = sc = er = ec = 0
        empty = 0
        self.output = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x,y,visited,e):
            if x == er and y == ec:
                if e == empty+1:
                    self.output += 1
                return
            if 0<=x<m and 0<=y<n and grid[x][y] != -1 and (x,y) not in visited:
                visited.add((x,y))
                for dr,dc in directions:
                    dfs(dr+x,dc+y,visited,e+1)
                visited.remove((x,y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    er,ec = i,j
                elif grid[i][j] == 1:
                    sr,sc = i,j
                elif grid[i][j] == 0:
                    empty += 1
        dfs(sr,sc,visited,0)      
        return self.output

        