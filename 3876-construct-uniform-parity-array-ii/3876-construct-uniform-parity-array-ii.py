class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        if all(num%2 == 0 for num in nums1) or all(num%2 == 1 for num in nums1):
            return True
        n = len(nums1)
        odd = 1
        for num in nums1:
            if num%2 == 1:
                odd = num 
                break
        for i in range(len(nums1)):
            if nums1[i] % 2 == 0 and nums1[i] - odd >= 1:
                nums1[i] = nums1[i] - odd
        return all(num%2 == 1 for num in nums1)
                


        

        