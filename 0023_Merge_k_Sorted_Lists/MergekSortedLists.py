# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        k = len(lists)
        interval = 1

        print(k)

        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if k > 0 else None

    def merge2Lists(self, l1, l2):
        head = ListNode(0)
        point = head

        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next

        if not l1:
            point.next = l2
        else:
            point.next = l1

        return head.next
