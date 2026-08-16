class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        f = [0,0,0]
        for s in stones:
            f[s%3] += 1
        if f[0]%2 == 0:
            return f[1] > 0 and f[2] > 0
        return abs(f[1]-f[2]) > 2
        