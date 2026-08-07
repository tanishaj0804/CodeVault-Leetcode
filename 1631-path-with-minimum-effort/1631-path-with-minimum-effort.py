class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0])
        dist = [[float('inf')]*n for _ in range(m)]
        heap = [(0,0,0)]   #effort,row,col 
        dist[0][0] = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            effort,r,c = heapq.heappop(heap)
            if effort > dist[r][c]:
                continue
            if r == m-1 and c == n-1:
                return effort
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    newe = max(effort,diff)
                    if newe < dist[nr][nc]:
                        dist[nr][nc] = newe
                        heapq.heappush(heap,(newe,nr,nc))
        return 0
