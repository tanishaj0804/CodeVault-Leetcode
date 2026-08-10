class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        l = 0
        r = len(numbers)-1
        while l<=r:
            val = numbers[l]+numbers[r]
            if target == val:
                ans.append(l+1)
                ans.append(r+1)
                break
            if val < target:
                l += 1
            else:
                r -= 1
        return ans

        