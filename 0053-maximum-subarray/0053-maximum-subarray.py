class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = 0
        for num in nums:
            curr = max(num,curr+num)
            ans = max(ans,curr)
        return ans

