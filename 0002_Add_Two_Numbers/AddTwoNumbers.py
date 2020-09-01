# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        node = ListNode()
        p = l1
        q = l2
        carry = 0
        current_node = node

        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = x + y + carry
            carry = sum // 10
            current_node.next = ListNode(sum % 10)
            current_node = current_node.next

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        if carry > 0:
            current_node.next = ListNode(carry, None)

        return node.next
