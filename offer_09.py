class CQueue:

    def __init__(self):
        self.stack_0 = []
        self.stack_1 = []


    def appendTail(self, value: int) -> None:
        self.stack_0.append(value)


    def deleteHead(self) -> int:
        if self.stack_0 or self.stack_1:
            if self.stack_1:
                return self.stack_1.pop()
            else:
                while self.stack_0:
                    self.stack_1.append(self.stack_0.pop())
                return self.stack_1.pop()
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()