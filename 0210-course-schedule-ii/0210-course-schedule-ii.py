class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        df = [0]*numCourses
        for course,pre in prerequisites:
            graph[pre].append(course)
            df[course] += 1
        q = deque([i for i in range(numCourses) if df[i] == 0])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for n in graph[curr]:
                df[n] -= 1
                if df[n] == 0:
                    q.append(n)
        return res if len(res) == numCourses else []