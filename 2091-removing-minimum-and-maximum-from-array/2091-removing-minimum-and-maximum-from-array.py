class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 1
        minv = min(nums)
        maxv = max(nums)
        id1 = nums.index(minv)
        id2 = nums.index(maxv)
        l = min(id1,id2)
        r = max(id1,id2)
        return min(r+1,n-l,l+1+n-r)
# removing from front -> largest index + 1
# removing from back -> len(nums) - smallest index
# removing from both directions, front -> smallest+1  +    back -> len(nums) - largest
        