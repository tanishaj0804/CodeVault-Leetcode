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
        mins = 0
        visited = [[False]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:
                for _ in range(len(q)):
                    r,c = q.popleft()   #pop from beginning not end 
                    for dr,dc in directions:
                        nr = r+dr
                        nc = c+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            fresh -= 1
                mins += 1
        return mins-1 if fresh == 0 else -1    