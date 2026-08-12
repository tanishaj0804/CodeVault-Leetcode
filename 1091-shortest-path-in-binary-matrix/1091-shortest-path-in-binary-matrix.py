class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if grid[0][0] == 0 and n == 1:
            return 1
        direction = [(0,1),(0,-1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        q = deque()
        visited = [[False]*n for _ in range(n)]
        q.append((0,0,1))  #row,col,path
        visited[0][0] = True
        while q:
            r,c,l = q.popleft()
            if r == n-1 and c == n-1:
                return l
            for dr,dc in direction:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr,nc,l+1))
        return -1
        