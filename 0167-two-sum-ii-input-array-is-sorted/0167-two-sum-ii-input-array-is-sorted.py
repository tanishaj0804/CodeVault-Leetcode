class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        sumv = 0
        l = 0
        r = len(numbers)-1
        while l<r:
            sumv = numbers[l]+numbers[r]
            if sumv == target:
                ans.append(l+1)
                ans.append(r+1)
            if sumv < target:
                l += 1
            else:
                r -= 1
        return ans


        