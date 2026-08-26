class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res =[]
        pacific = set()
        atlantic = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j,visited):
            visited.add((i,j))
            for dr, dc in directions:
                nr,nc = i+dr,j+dc
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                if (nr,nc) in visited:
                    continue
                if heights[nr][nc] < heights[i][j]:
                    continue
                dfs(nr,nc,visited)
        for i in range(rows):
            dfs(i, 0, pacific)

        for j in range(cols):
            dfs(0, j, pacific)

        for i in range(rows):
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(rows - 1, j, atlantic)
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res

        