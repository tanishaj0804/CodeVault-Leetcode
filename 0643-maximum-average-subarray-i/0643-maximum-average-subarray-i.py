class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = sum(nums[:k])
        mavg = ans/float(k)
        for i in range(k,len(nums)):
            ans += nums[i]
            ans -= nums[i-k]
            mavg = max(mavg,ans/float(k))
        return mavg
        