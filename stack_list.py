class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit
        
    def isEmpty(self):
        return len(self.stack) <= 0
        
    def push(self, item):
        if len(self.stack) >= self.limit:
            print("Stack overflow")
            return 0
        else:
            self.stack.append(item)
            print("Stack Push ", self.stack)
            
    def pop():
        if len(self.stack) <= 0:
            print("Stack Underflow")
            return 0
            
        else:
            return self.stack[-1]
            
    def size(self):
        return len(self.stack)
        
        
new_stack = Stack(5)
new_stack.push(1)
new_stack.push(2)
            
