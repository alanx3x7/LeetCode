# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(0, None)
        head = dummy

        while not (l1 is None and l2 is None):

            if l1 is None:
                head.next = l2
                l2 = l2.next
            elif l2 is None:
                head.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next

            head = head.next

        return dummy.next

