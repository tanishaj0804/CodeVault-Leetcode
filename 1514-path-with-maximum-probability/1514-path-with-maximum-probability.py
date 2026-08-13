class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj =[[] for _ in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1],succProb[i]))
            adj[edges[i][1]].append((edges[i][0],succProb[i]))
        dist =[float('-inf')]*n
        dist[start_node] = 1.0
        heap =[(-1.0,start_node)]
        while heap:
            nprob,node = heapq.heappop(heap)
            prob = -nprob
            if prob < dist[node]:
                continue
            if node == end_node:
                return prob
            for nei,p in adj[node]:
                newp = prob*p
                if newp > dist[nei]:
                    dist[nei] = newp
                    heapq.heappush(heap,(-newp,nei))
        return 0.0
        