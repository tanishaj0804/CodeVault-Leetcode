class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for num in nums:
            if freq[num] == 1:
                return num
        