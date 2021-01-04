class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []
        self.size = 0

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.size == 0 or x < self.min_data[-1]:
            self.min_data.append(x)
        else:
            self.min_data.append(self.min_data[-1])
        self.size += 1

    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()
        self.size -= 1

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.min_data[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()