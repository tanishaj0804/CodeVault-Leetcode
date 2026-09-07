class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums