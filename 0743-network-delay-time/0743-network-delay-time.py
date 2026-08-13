class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        dist =[float('inf')]*(n+1)
        dist[k] = 0
        heap = [(0,k)]
        while heap:
            cost,node = heapq.heappop(heap)
            if cost > dist[node]:
                continue 
            for nei,w in adj[node]:
                newc = w+cost
                if newc < dist[nei]:
                    dist[nei] = newc
                    heapq.heappush(heap,(newc,nei))
        ans = max(dist[1:])
        if ans == float('inf'):
            return -1
        return ans

        