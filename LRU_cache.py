
class LLNode:
    def __init__(self, key, data, next_node, prev_node):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
        self.key = key
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.occupancy = 0
        self.head = None
        self.tail = None
        
    def use_item(self, node):
        print("use item",node.key, node.data)
        print("head", self.head.key)
        print("tail", self.tail.key)
        #remove node from current place in queue
        if node is self.tail:
            return
        elif node is self.head:
            self.head = self.head.next_node
            node.next_node.prev_node = None
        else:
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
        
        #put node at back of queue (impl by LL)
        self.tail.next_node = node
        node.next_node = None
        node.prev_node = self.tail
        self.tail = node
            
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print("get---------",key)
        if key in self.cache:
            node = self.cache[key]
            self.use_item(node)
            return node.data
        else:
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print("put---------",key, value)
        
        # new item
        if key not in self.cache:
            # add item to cache
            self.occupancy +=1
            node = LLNode(key, value,None, None)
            self.cache[key] = node
            
            #if cache is empty, then we are done
            if not self.head:
                self.head = node
                self.tail = node
                return 
            
            print("add item to end", self.tail.key)
            #put item at end
            self.tail.next_node = node
            print("prev next key", self.tail.next_node.key)
            node.prev_node = self.tail
            self.tail = node
            print("new end key", self.tail.key)
            
            # evict oldest item
            if self.occupancy > self.capacity:
                # remove from cache
                self.cache.pop(self.head.key)
                self.occupancy -=1
                # update FIFO queue
                self.head = self.head.next_node
                self.head.prev_node = None
            
            
        #update exisiting item
        else:
            node = self.cache[key]
            node.data = value
            self.use_item(node)        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)