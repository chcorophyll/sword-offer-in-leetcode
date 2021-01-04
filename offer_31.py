class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_stack, index = [], 0
        for num in pushed:
            push_stack.append(num)
            while push_stack and push_stack[-1] == popped[index]:
                push_stack.pop()
                index += 1
        return not push_stack