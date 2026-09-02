from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        ns = len(set(nums))
        if n == ns:
            return False
        return True

        