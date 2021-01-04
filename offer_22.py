# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return None
        first_node = head
        for i in range(k-1):
            if first_node.next != None:
                first_node = first_node.next
            else:
                return None
        second_node = head
        while first_node.next != None:
            first_node = first_node.next
            second_node = second_node.next
        return second_node