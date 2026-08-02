class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = [0] * n

        # Store (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def mergeSort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            mergeSort(left, mid)
            mergeSort(mid + 1, right)

            merge(left, mid, right)

        def merge(left, mid, right):
            temp = []
            i = left
            j = mid + 1

            # Number of right-half elements already placed
            rightCount = 0

            while i <= mid and j <= right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    rightCount += 1
                    j += 1
                else:
                    counts[arr[i][1]] += rightCount
                    temp.append(arr[i])
                    i += 1

            while i <= mid:
                counts[arr[i][1]] += rightCount
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[left + k] = temp[k]

        mergeSort(0, n - 1)
        return counts


        