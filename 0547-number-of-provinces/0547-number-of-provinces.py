class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        count = 0
        def dfs(node):
            for nei in range(n):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    visited[nei]=True
                    dfs(nei)
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        return count
        