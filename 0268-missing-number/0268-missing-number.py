class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = sum(nums)
        expect = n*(n+1)//2
        return expect-actual