class Moving_Average:
    def __init__(self, window_size ): 
        self.queue = []
        self.window_size = window_size
        self.sum = 0
    def next(self, num):
        self.queue.append(num)
        if len(self.queue) > self.window_size:
            self.sum -= self.queue.pop(0) # remove poped item from sum
        #add new item to sum
        self.sum += num
            


        
        return self.sum/len(self.queue)


ma = Moving_Average(3)
print(ma.next(1))
print(ma.next(2))
print(ma.next(3))
print(ma.next(1))