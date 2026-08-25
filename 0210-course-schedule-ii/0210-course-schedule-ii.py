class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj =[[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        res = []
        q = deque()
        count = 0
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            res.append(node)
            count += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if count == numCourses else []
        