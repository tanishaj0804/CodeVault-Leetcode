# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        lsort = float('-inf')
        while curr is not None:
            if curr.val >= lsort:
                lsort = curr.val
                prev = curr
                curr = curr.next
                continue
            pos = dummy
            while curr.val >= pos.next.val:
                pos = pos.next
            prev.next = curr.next
            curr.next = pos.next
            pos.next = curr
            curr = prev.next

        return dummy.next

        