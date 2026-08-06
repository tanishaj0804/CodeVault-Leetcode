class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adj =[[] for _ in range(n)]
        for source, destination, price in flights:
            adj[source].append((destination,price))
        heap = [(0,src,0)]   #[cost,city,stops]
        visited = {}
        while heap:
            cost,city,stops = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops > k:
                continue
            if city in visited and visited[city] <= stops:
                continue
            visited[city] = stops
            for nex,pric in adj[city]:
                heapq.heappush(heap,(cost+pric,nex,stops+1))
        return -1