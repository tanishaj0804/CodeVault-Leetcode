class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c = q.popleft()
            for dr,dc in direction:
                nr,nc = r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr,nc))
        return mat

        