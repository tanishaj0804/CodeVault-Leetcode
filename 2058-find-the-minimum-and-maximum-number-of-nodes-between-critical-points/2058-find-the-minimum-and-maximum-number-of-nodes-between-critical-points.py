# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return -[-1,-1]
        arr = []
        ans = []
        while head:
            arr.append(head.val)
            head = head.next
        if len(arr) <= 2:
            return [-1,-1]
        for i in range(1,len(arr)-1):
            if arr[i] < arr[i+1] and arr[i] < arr[i-1]:
                ans.append(i)
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                ans.append(i)
        if len(ans) <= 1:
            return [-1,-1]
        ans.sort()
        mind = float('inf')
        for i in range(1,len(ans)):
            mind = min(mind,ans[i]-ans[i-1])
        return [mind,ans[-1] - ans[0]]
        
        