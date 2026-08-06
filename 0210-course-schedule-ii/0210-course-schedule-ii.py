class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj =[[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(indegree[i])
        res = []
        while q:
            curr = q.pop()
            res.append(curr)
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
