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
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        temp = head
        for i in range(len(arr)):
            temp.val = arr[i]
            temp = temp.next

        return head
        