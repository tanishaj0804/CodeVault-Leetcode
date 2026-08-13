class Solution:
    def countRestrictedPaths(self, n, edges):
        MOD = 10**9+7
        adj =[[] for _ in range(n+1)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist = [float('inf') for _ in range(n+1)]
        dist[n] = 0
        heap = [(0,n)]
        while heap:
            d,node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nei,w in adj[node]:
                neww = w+d
                if neww < dist[nei]:
                    dist[nei] = neww
                    heapq.heappush(heap,(neww,nei))
        dp = [-1]*(n+1)
        dp[n] = 1
        def dfs(node):
            if dp[node] != -1:
                return dp[node]
            ways = 0
            for nei,w in adj[node]:
                if dist[node] > dist[nei]:
                    ways += dfs(nei)
            dp[node] = ways%MOD
            return dp[node]
        return dfs(1)