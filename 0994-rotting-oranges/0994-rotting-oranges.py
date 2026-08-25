class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        minutes = 0
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        if fresh == 0:
            return minutes
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr,nc))
                        fresh -= 1
            minutes += 1
        return minutes-1 if fresh == 0 else -1       