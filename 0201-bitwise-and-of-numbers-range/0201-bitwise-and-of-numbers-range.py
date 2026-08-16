class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left!= right:
            left = left >> 1   #left/2
            right = right >> 1  #right/2
            shift += 1
        return left << shift