# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        lis = []
        while head:
            lis.append(head.val)
            head=head.next
        ans = []
        for num in lis:
            if num < x:
                ans.append(num)
        for num in lis:
            if num >= x:
                ans.append(num)
        for num in ans:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

            