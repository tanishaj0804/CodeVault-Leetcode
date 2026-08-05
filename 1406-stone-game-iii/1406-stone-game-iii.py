class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp =[0]*(n+1)
        for i in range(n-1,-1,-1):
            best = float('-inf')
            sumv = 0
            for k in range(1,4):
                if i+k > n:
                    break
                sumv += stoneValue[i+k-1]
                best = max(best,sumv-dp[i+k])
            dp[i] = best
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

        