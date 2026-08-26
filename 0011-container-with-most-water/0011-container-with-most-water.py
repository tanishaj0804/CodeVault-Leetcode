class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0
        maxv = 0
        while l<=r:
            width = r-l
            length = min(height[l],height[r])
            area = width*length
            maxv = max(area, maxv)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxv
        