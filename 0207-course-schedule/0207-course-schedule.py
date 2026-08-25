class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj =[[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        q = deque()
        count = 0
        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            new = q.popleft()
            count += 1
            for nei in adj[new]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return count == numCourses


        