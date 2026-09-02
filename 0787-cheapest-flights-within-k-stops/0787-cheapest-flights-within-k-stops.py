class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,cost in flights:
            adj[u].append((v,cost))
        dist = [float('inf')]*n
        dist[src] = 0
        visited = {}
        heap = [[0,src,0]]   #cost,destination,k
        while heap:
            cost, city,stop = heapq.heappop(heap)
            if city == dst:
                return cost
            if stop > k:
                continue
            if city in visited and visited[city] <= stop:
                continue
            visited[city] = stop
            for nex,pric in adj[city]:
                heapq.heappush(heap,(cost+pric,nex,stop+1))
        return -1
