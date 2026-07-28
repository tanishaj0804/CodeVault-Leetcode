class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if len(piles) == h:
            return max(piles)
        l,r = 1,max(piles)
        ans = r
        while l<=r:
            mid = (l+r)//2
            hours = sum((p+mid-1)//mid for p in piles)
            if hours <= h:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
        
        