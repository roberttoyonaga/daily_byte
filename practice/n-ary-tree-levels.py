# level order traversal of an n-ary tree
# I DID NOT IMPLEMENT THIS 

#need a n-ary tree node class. I didnt want to make this


from collections import deque
from BST import *

def gather_levels_from_tree(root):
    queue = deque([root])
    levels = []

    while queue:
        size = len(queue) # amount of nodes in current level
        current_lvl = []
        
        #iterate through all nodes in current level
        for i in  range(size):

            #process current node
            node = queue.popleft()
            current_lvl.append(node.data)

            #add nodes in subsequent level to queue
            
            # here we go through all nodes in our current node's list of child pointers and add them to the queue

        levels.append(current_lvl)
    
    return levels