class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for num in nums:
            res += [curr + [num] for curr in res]
        return res
                

        