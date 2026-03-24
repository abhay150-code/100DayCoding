class MyStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)
        
        while self.stack1:
            self.stack2.append(self.stack1.pop(0))
        
        self.stack1, self.stack2 = self.stack2, self.stack1

    def pop(self) -> int:
        return self.stack1.pop(0)

    def top(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()