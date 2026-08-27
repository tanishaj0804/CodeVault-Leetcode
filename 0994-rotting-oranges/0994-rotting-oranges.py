class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0
        visited = [[False]*cols for _ in range(rows)]
        directions =[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+r,dc+c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr,nc))
                        fresh -= 1
            minutes += 1
        return minutes-1 if fresh==0 else -1