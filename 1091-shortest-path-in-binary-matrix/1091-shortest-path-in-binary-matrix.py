class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid) 
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if grid[0][0] == 0 and n==1:
            return 1
        visited = [[False]*n for _ in range(n)]
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        q = deque()
        q.append((0,0,1))
        while q:
            x,y,l = q.popleft()
            if x == n-1 and y == n-1:
                return l
            for dr,dc in direction:
                nr,nc = dr+x,dc+y
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc,l+1))
        return -1
        
        