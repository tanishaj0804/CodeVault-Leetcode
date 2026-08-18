# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        N = len(stack)
        del stack[N-n]
        dummy = ListNode(0)
        temp = dummy
        for val in stack:
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next