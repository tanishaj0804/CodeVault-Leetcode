# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [float('inf'),-1]
        first = -1
        last = -1 
        i = 1
        prev,curr,nex = head,head.next,head.next.next
        while nex:
            if (curr.val < prev.val and curr.val < nex.val) or (curr.val > prev.val and curr.val > nex.val) :
                if first == -1:
                    first = i
                if last != -1:
                    ans[0] = min(ans[0],i-last)
                last = i
            prev = curr
            curr = nex
            nex = nex.next
            i += 1
        if first == -1 or first == last:
            return [-1,-1]
        ans[1] = last-first
        return ans

        