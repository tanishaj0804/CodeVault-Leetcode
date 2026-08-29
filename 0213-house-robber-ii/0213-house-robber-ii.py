class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        nums1 = nums[:n-1]
        nums2 = nums[1:]
        def solve(arr):
            if len(arr) <= 2:
                return max(arr)
            prev = arr[0]
            curr = max(arr[0],arr[1])
            for i in range(2,len(arr)):
                sol = max(curr,arr[i]+prev)
                prev,curr = curr,sol
            return curr
        first = solve(nums1)
        second = solve(nums2)
        return max(first,second)