class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
       self.stack.append(x)

       if not self.min_stack or x <= self.min_stack[-1]:
        self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return
        
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()

    def top(self):
        if not self.stack:
           return 0
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()