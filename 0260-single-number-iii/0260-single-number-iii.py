class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        x &= -x
        res = [0]*2
        for num in nums:
            if num & x == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
                
        