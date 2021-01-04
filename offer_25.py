# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy_head = ListNode(0)
        merge_head = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                merge_head.next = l1
                merge_head = merge_head.next
                l1 = l1.next
            else:
                merge_head.next = l2
                merge_head = merge_head.next
                l2 = l2.next
        if l1:
            while l1:
                merge_head.next = l1
                merge_head = merge_head.next
                l1 = l1.next
        if l2:
            while l2:
                merge_head.next = l2
                merge_head = merge_head.next
                l2 = l2.next
        return dummy_head.next