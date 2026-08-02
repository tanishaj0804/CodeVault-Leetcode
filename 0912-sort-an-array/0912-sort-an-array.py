class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(nums, l, mid, r):
            n1 = mid - l + 1
            n2 = r - mid

            l1 = [0] * n1
            l2 = [0] * n2

            # Copy data into temporary arrays
            for i in range(n1):
                l1[i] = nums[l + i]

            for j in range(n2):
                l2[j] = nums[mid + 1 + j]

            i = 0
            j = 0
            k = l

            # Merge the two arrays
            while i < n1 and j < n2:
                if l1[i] <= l2[j]:
                    nums[k] = l1[i]
                    i += 1
                else:
                    nums[k] = l2[j]
                    j += 1
                k += 1

            # Copy remaining elements of l1
            while i < n1:
                nums[k] = l1[i]
                i += 1
                k += 1

            # Copy remaining elements of l2
            while j < n2:
                nums[k] = l2[j]
                j += 1
                k += 1

        def mergeSort(nums, l, r):
            if l < r:
                mid = (l + r) // 2

                mergeSort(nums, l, mid)
                mergeSort(nums, mid + 1, r)

                merge(nums, l, mid, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums