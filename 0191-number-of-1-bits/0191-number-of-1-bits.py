class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
       """
        cnt = []
        while n:
            cnt.append(n%2)
            n = n//2
        return cnt.count(1)

        