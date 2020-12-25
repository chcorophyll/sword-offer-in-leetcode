# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        origin_head = head
        stop = False
        previous = None
        while head and not stop:
            if head.val == val:
                stop = True
                break
            previous = head
            head = head.next
        if stop:
            if previous == None:
                head = head.next
                return head
            else:
                previous.next = head.next
                return origin_head
        else:
            return None