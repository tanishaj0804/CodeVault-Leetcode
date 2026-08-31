class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i,n in enumerate(nums):
            while q and nums[q[-1]] <= n:
                q.pop()
            while q and q[0] <= i-k:
                q.popleft()
            q.append(i)
            if i>= k-1:
                ans.append(nums[q[0]])
        return ans
        