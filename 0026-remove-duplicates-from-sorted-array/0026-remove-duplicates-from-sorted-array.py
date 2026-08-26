class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        while j <len(nums):
            if nums[j] == nums[j-1]:
                nums.pop(j)
            else:
                j += 1
        return len(nums)


        