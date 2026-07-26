class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        first = [1]
        result.append(first)
        for i in range(1,numRows):
            prev=result[i-1]
            curr = [1]
            for j in range(1,i):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            result.append(curr)
        return result