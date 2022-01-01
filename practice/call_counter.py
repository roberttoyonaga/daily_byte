from collections import deque

class Call_Counter:
    def __init__(self ): 
        self.n_calls = 0
        self.queue = deque()
        self.period = 3000
    def ping(self, t_ms):
        #deal with new call
        self.n_calls += 1
        self.queue.append(t_ms)

        while self.queue: #implicitely converts to bool. false if empty
            last_time =  self.queue[0]
            if (t_ms - last_time) >= self.period:
                self.queue.popleft()
                self.n_calls -= 1
            else:
                break
        
        return self.n_calls

cntr = Call_Counter()
print(cntr.ping(0))
print(cntr.ping(1000))
print(cntr.ping(2000))
print(cntr.ping(3000))
print(cntr.ping(3001))
print(cntr.ping(3002))
print(cntr.ping(3003))
print(cntr.ping(5000))



