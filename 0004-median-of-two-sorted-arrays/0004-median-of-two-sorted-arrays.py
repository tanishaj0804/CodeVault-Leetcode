class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = len(nums1) +len(nums2)
        union_list = [0]*x
        for i in range (0,len(nums1)):
            union_list[i] = nums1[i]
        for j in range (0,len(nums2)):
            union_list[len(nums1) + j] = nums2[j]
        sorted_list = sorted(union_list)
        if x % 2 != 0:
            y = x//2
            return float(sorted_list[y])
        else:
            mid1 = sorted_list[x//2-1]
            mid2 = sorted_list[x//2]
            return (mid1+mid2)/2.0
        