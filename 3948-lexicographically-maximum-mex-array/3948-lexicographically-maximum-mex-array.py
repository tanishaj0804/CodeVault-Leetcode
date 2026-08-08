class Solution(object):
    def maximumMEX(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        res = []
        i = 0
        n = len(nums)
        while i < n:
            maxmex = 0
            while freq[maxmex] >0:
                maxmex += 1
            if maxmex == 0:
                res.append(0)
                freq[nums[i]] -= 1
                i += 1
                continue
            seen = set()
            j = i
            while j<= n and len(seen) < maxmex:
                if nums[j] < maxmex:
                    seen.add(nums[j])
                j += 1
            for k in range(i,j):
                freq[nums[k]] -= 1
            res.append(maxmex)
            i=j
        return res