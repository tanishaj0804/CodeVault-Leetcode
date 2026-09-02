class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        maxv = 0
        for num in nums:
            if freq[num] > n//2:
                return num
                