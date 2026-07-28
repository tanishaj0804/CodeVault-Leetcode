class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        for courses, pre in prerequisites:
            adj[pre].append(courses)
        vis = [False]*numCourses
        path = [False]*numCourses

        def dfs(node):
            vis[node] = path[node] = True
            for n in adj[node]:
                if not vis[n]:
                    if dfs(n):
                        return True
                elif path[n]:
                    return True
            path[node] = False
            return False
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False
        return True