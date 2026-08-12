class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #Bipartite == no 2 adjacent nodes should have same color, if then do return False
        n=len(graph)
        color = [-1]*n
        def dfs(node,c):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei,1-c):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        return True
        