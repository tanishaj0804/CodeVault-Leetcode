class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l =0
        r = n-1
        leftm = rightm = 0
        ans = 0
        while l<r:
            leftm = max(leftm,height[l])
            rightm = max(rightm,height[r])
            if leftm < rightm:
                ans += leftm - height[l]
                l += 1
            else:
                ans += rightm - height[r]
                r -= 1
        return ans

        