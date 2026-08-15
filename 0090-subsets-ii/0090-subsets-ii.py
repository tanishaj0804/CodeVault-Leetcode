class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        res.append([])
        for num in nums:
            sub = []
            for curr in res:
                news = curr + [num]
                if news not in res:
                    sub.append(news)
            res.extend(sub)
        return res