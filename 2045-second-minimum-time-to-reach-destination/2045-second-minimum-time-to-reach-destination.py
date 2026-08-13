class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        adj = [[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        heap = [(0,1)]
        dist =[[float('inf'),float('inf')] for _ in range(n+1)]
        dist[1][0] = 0
        while heap:
            curr,node = heapq.heappop(heap)
            if curr > dist[node][1]:
                continue
            if node == n and curr == dist[node][1]:
                return curr
            for nei in adj[node]:
                curr_t = curr
                if (curr_t//change)%2==1:
                    curr_t += change - (curr_t%change)
                curr_t += time
                
                if curr_t < dist[nei][0]:
                    dist[nei][1] = dist[nei][0]
                    dist[nei][0] = curr_t
                    heapq.heappush(heap,(curr_t,nei))
                elif dist[nei][0] < curr_t < dist[nei][1]:
                    dist[nei][1] = curr_t
                    heapq.heappush(heap, (curr_t, nei))
        return -1
    