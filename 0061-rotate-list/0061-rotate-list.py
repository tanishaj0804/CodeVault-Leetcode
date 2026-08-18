# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        k = k%count  #if k>count then avoid unnecessary rotations
        if k == 0:
            return head
        temp.next = head
        steps = count-k
        tail = head
        for _ in range(steps-1):
            tail = tail.next
        nhead = tail.next
        tail.next = None
        return nhead
        