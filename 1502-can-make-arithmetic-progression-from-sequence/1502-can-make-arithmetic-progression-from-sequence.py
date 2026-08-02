class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        for i in range(n-1):
            minv = i
            for j in range(i+1,n):
                if arr[j] < arr[minv]:
                    minv = j
            arr[i],arr[minv] = arr[minv],arr[i]
        diff = arr[1] - arr[0]
        for i in range(1,n-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True
        