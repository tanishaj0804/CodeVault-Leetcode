from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c]+1
                    q.append((nr,nc))
        return mat

        