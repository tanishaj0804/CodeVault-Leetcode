class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = -1
        while n:
            if n%2 == 0:
                n = n//2
            else:
                if n == 3:
                    n -= 1
                elif (n&2):
                    n += 1
                else:
                    n -= 1
            cnt += 1
        return cnt

        