from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        frequent = dict(sorted(freq.items(),key = lambda x:x[1],reverse= True))
        return list(frequent.keys())[:k]
        
        