class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m=len(classroom)
        n = len(classroom[0])
        idx = [[0]*n for  _ in range(m)]
        sx,sy = 0,0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx,sy = i,j
                elif classroom[i][j] == 'L':
                    idx[i][j] = 1<<cnt
                    cnt += 1
        full = 1<<cnt
        best = [[[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)]
        best[sx][sy][0] = energy
        q = deque()
        q.append((sx,sy,0,energy,0))
        while q:
            x,y,mask,e,step = q.popleft()
            if mask == full-1:
                return step
            if e == 0:
                continue
            for dr,dc in directions:
                nx,ny = x+dr,y+dc
                if nx<0 or nx>=m or ny<0 or ny>=n or classroom[nx][ny] == 'X':
                    continue
                ne = energy if classroom[nx][ny] == 'R' else e-1
                nmask = mask | idx[nx][ny]
                if ne > best[nx][ny][mask]:
                    best[nx][ny][mask] = ne
                    q.append((nx,ny,nmask,ne,step+1))
        return -1
        