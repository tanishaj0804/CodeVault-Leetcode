class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s == 0:
            return 0
        if s<1 or s>9*n:
            return -1
        digit = []
        for i in range(n):
            val = min(9,s)
            digit.append(str(val))
            s-= val
        return int("".join(digit))
        