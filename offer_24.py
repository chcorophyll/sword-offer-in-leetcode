# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        reverse_head = None
        while head:
            temp = head.next
            head.next = reverse_head
            reverse_head = head
            head = temp
        return reverse_head