class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for j in range(1,n+1):
            if j-1>=0:
                dp[j] = min(dp[j],dp[j-1]+costs[j-1]+1)
            if j-2>=0:
                dp[j] = min(dp[j],dp[j-2]+costs[j-1]+4)
            if j-3>=0:
                dp[j] = min(dp[j],dp[j-3]+costs[j-1]+9)
        return dp[n]
        