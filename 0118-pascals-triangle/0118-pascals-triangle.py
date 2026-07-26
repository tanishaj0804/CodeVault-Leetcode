class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prev = self.generate(numRows-1)
        row = [1]*numRows
        for i in range(1,numRows-1):
            row[i] = prev[-1][i-1]+prev[-1][i]
        prev.append(row)
        return prev
        