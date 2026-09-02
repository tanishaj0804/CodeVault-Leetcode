class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n = len(nums1)
        nums2 = [0]*n
        even = None
        odd = None
        for num in nums1:
            if num%2 == 0:
                even = num
            else:
                odd = num
        if even is None or odd is None:
            return True

        for i in range(len(nums1)):
            if nums1[i]%2 == 1:
                nums2[i] = nums1[i] - even
            else:
                nums2[i] = nums1[i] - odd
        return all(num%2 == 1 for num in nums2)
        
        