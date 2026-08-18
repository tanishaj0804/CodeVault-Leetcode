class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter(nums)
        n = len(nums)
        if k == 1:
            ans  = -1
            for num in nums:
                if freq[num] == 1:
                    ans = max(ans,num)
            return ans
        if k == n:
            return max(nums)
        first = nums[0] if freq[nums[0]] == 1 else -1
        sec = nums[-1] if freq[nums[-1]] == 1 else -1
        return max(first,sec)
        