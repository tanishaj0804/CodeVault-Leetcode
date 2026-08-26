class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if grid[0][0] == 0 and n==1:
            return 1
        q = deque([(0,0,1)])
        visited = [[False]*n for _ in range(n)]
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        while q:
            r,c,l = q.popleft()
            if r == n-1 and c ==n-1:
                return l
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] != 1:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr,nc,l+1))        
        return -1