class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0 
        n = len(height)
        left = 0
        right = n-1
        while left < right:
                width = right - left
                length = min(height[left],height[right])
                area = length*width
                max_area = max(max_area, area)
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
        return max_area


        