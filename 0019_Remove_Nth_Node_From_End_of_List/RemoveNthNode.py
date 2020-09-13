# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0, head)
        list_len = 0
        first = head

        while not first is None:
            list_len += 1
            first = first.next

        node_num = 0
        first = dummy
        while node_num < list_len - n:
            first = first.next
            node_num += 1

        first.next = first.next.next

        return dummy.next
