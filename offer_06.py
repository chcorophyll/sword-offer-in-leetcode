# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        def reverse_head(head_node, result_list):
            if head_node != None:
                if head_node.next != None:
                    reverse_head(head_node.next, result_list)
                result_list.append(head_node.val)
        result = []
        reverse_head(head, result)
        return result