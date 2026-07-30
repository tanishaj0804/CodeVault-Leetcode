class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        common = set(edges[0])  # the first row
        for row in edges:
            common &= set(row)   # {1,2} & {2,3} = 2
        ans = common.pop()
        return ans