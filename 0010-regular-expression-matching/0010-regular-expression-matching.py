class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def match(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(p):
                return i == len(s) #return only if string also completed
            first_match = (i<len(s) and (s[i] == p[j] or p[j]=='.'))
            if j+1 < len(p) and p[j+1] == '*':
                ans = match(i,j+2) or (first_match and match(i+1,j))
            else:
                ans = first_match and match(i+1,j+1)

            memo[(i,j)] = ans
            return ans
        return match(0,0)