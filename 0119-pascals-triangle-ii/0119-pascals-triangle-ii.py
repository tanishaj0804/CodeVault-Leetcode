class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex-1)
        curr = [1]*(rowIndex+1)
        for i in range(1,rowIndex):
            curr[i] = prev[i-1]+prev[i]
        prev.append(curr)
        return prev[-1]
        