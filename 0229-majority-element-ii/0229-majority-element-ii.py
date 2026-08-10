class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = n/3
        freq = Counter(nums)
        ans = []
        for num in nums:
            if freq[num] > i:
                ans.append(num)
        ans = set(ans)
        return list(ans)