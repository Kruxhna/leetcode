class MinStack(object):

    def __init__(self):
        self.stack =[]

    def push(self, val):
        if not self.stack :
            new_min = val
        else :
            curr_min = self.stack[-1][1]
            new_min = min(val,curr_min)
        
        self.stack.append((val,new_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack :
            self.stack.pop()
        

    def top(self):
        if self.stack :
            return self.stack[-1][0]
        return None
        

    def getMin(self):
        if self.stack :
            return self.stack[-1][1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()