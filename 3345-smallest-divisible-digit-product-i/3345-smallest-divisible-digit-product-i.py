class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        maxv = float('inf')
        while n < maxv:
            prod = 1
            for digit in str(n):
                prod *= int(digit)
            if prod%t == 0:
                return n
            n += 1
        
        