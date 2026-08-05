class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        edges =[[] for _ in range(n)]
        for u,v in invocations:
            edges[u].append(v)
        sus = [False]*n
        def DFS(node):
            sus[node] = True
            for nei in edges[node]:
                if not sus[nei]:
                    DFS(nei)
        DFS(k)
        for u,v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))
        ans = []
        for i in range(n):
            if not sus[i]:
                ans.append(i)
        return ans
    

        