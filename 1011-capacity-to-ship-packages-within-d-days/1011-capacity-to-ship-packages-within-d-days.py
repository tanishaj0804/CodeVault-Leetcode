class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        while l<r:
            mid = (l+r)//2
            need = 1
            curr = 0
            for w in weights:
                if curr+w > mid:
                    need += 1
                    curr = 0
                curr += w
            if need > days:
                l = mid+1
            else:
                r = mid
        return l
        
        