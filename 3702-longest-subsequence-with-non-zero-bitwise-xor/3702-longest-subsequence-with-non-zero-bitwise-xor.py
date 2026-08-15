class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        if ans != 0:
            return len(nums)
        if any(nums):
            return len(nums)-1
        return 0
        
