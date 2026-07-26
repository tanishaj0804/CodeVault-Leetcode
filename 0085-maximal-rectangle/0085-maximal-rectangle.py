class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def maxRectangle(dp):
            stack =[]
            ar = 0
            n = len(dp)
            for i in range(n+1):
                curr = 0 if i==n else dp[i]
                while stack and curr < dp[stack[-1]]:
                    height = dp[stack.pop()]
                    if not stack:
                        width = i
                    else:
                        width = i-stack[-1]-1
                    ar = max(ar,height*width)
                stack.append(i)
            return ar
        area = 0
        m,n = len(matrix),len(matrix[0])
        if not matrix or not matrix[0]:
            return 0
        dp = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j] += 1
            area = max(area,maxRectangle(dp))
        return area
