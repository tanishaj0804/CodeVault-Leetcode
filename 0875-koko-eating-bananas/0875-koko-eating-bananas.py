class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if len(piles) == h:
            return max(piles)
        minv = 1
        maxv = ans = max(piles)
        while minv <= maxv:
            mid = (minv+maxv) // 2
            hours = 0
            for pile in piles:
                hours += (pile+mid-1)//mid
            if hours > h:
                minv = mid+1
            else:
                ans = mid
                maxv = mid-1
        return ans
        
        