class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        dest = n-1
        stack =[(0,[0])]
        res = []
        while stack:
            node,path = stack.pop()
            if node == dest:
                res.append(path)
            for nei in graph[node]:
                stack.append((nei,path+[nei]))
        return res
        
        