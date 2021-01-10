# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # def get_length(self, head):
    #     length = 0
    #     while head:
    #         length += 1
    #         head = head.next
    #     return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # if not headA or not headB:
        #     return None
        # length_a = self.get_length(headA)
        # length_b = self.get_length(headB)
        # if length_a >= length_b:
        #     length_differ = length_a - length_b
        #     head_long = headA
        #     head_short = headB
        # else:
        #     length_differ = length_b - length_a
        #     head_long = headB
        #     head_short = headA
        # while length_differ > 0:
        #     head_long = head_long.next
        #     length_differ -= 1
        # while head_long != None and head_short != None and head_long != head_short:
        #     head_long = head_long.next
        #     head_short = head_short.next
        # return head_long
        if not headA or not headB:
            return None
        index_a, index_b = headA, headB
        while index_a != index_b:
            index_a = index_a.next if index_a else headB
            index_b = index_b.next if index_b else headA
        return index_a