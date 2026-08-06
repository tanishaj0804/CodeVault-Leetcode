class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append((equations[i][1],values[i]))
            adj[equations[i][1]].append((equations[i][0],1/values[i]))
        def dfs(node, target):
            if node == target:
                return 1
            visited.add(node)
            for nei,val in adj[node]:
                if nei not in visited:
                    ans = dfs(nei,target)
                    if ans != -1:
                        return ans*val
            return -1
        res = []
        for src,dest in queries:
            if src not in adj or dest not in adj:
                res.append(-1.0)
                continue
            visited = set()
            ans = dfs(src,dest)
            res.append(ans)
        return res

        
        