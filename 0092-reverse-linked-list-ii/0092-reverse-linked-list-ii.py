# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lis = []
        while head:
            lis.append(head.val)
            head= head.next
        lis[left-1:right] = lis[left-1:right][::-1]
        dummy = ListNode(0)
        curr = dummy
        for num in lis:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

        