class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        dist = [float('inf')]*(n+1)
        heap = [(0,k)]
        dist[k] = 0
        while heap:
            time,node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for nei,wt in adj[node]:
                newt = time+wt
                if newt < dist[nei]:
                    dist[nei] = newt
                    heapq.heappush(heap,(newt,nei))
        ans = max(dist[1:])
        if ans == float('inf'):
            return -1
        return ans

        