class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
    
    def push(self, val: int) -> None:
        # pushes the element val onto the stack
        # We push a tuple at every step, the tuple contains min and current val
        if val < self.minimum:
            self.minimum = val
        
        self.stack.append((val,self.minimum))
        return

    def pop(self) -> None:
        # removes the lement on the top of the stack
        self.stack.pop()
        if not self.stack:
            self.minimum = float('inf')
        else:
            self.minimum = self.stack[-1][1]
        return 

    def top(self) -> int:
        # get the top element of the stack
        return self.stack[-1][0]


    def getMin(self) -> int:
        # retrieves minmum element in the stack
        ans = self.stack[-1][1]
        print(f"ans:{ans} and type is {type(ans)} ")
        return ans