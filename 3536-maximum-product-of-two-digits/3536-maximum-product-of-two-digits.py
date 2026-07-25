import math
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        m = sorted(n)
        return int(m[-1])*int(m[-2])        