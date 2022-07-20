# Using Two Stacks and Using 1 Stack

#Time and Space for all Methods : O(1) Time Complexity | O(1) Space Complexity
class MinStack:

    def __init__(self):
      # O(1) Time Complexity | O(n) Space Complexity for extra stack overall
        self.stack = []
        self.helperStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helperStack:
            self.helperStack.append(val)
        else:
            minVal = min(val,self.getMin())
            self.helperStack.append(minVal)
            
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.helperStack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        
    def getMin(self) -> int:
        if self.helperStack:
            return self.helperStack[-1]
        return None
        

 # Using 1 Stack 

class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        currMin = self.getMin()
        if currMin is None or val < currMin:
            currMin = val
        self.stack.append([val,currMin])
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        return None
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

