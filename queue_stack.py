from collections import deque

class Queue_Stack:
    def __init__(self ): 
        self.queue = deque()
    def pop(self):
        count =0 
        while count < len(self.queue) -1:
            self.queue.append(self.queue.pop())
            count+=1
        return self.queue.pop()
    def push(self, arg):
        self.queue.append(arg)
        
    def peek(self):
        count = 0 
        while count < len(self.queue) -1:
            self.queue.append(self.queue.pop())
            count+=1
        ret = self.queue.pop()
        self.queue.append(ret)
        return ret

    def empty(self):
        return len(self.queue)==0

stack = Queue_Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.empty())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())