from collections import deque
from BST import *

'''
use a "deque"  which supports stack and queue operations. This exists not just in python
'''
def zig_zag_traversal(root):
    queue = deque([root])
    levels = []
    count = 0

    while queue:
        size = len(queue) # amount of nodes in current level
        current_lvl = deque([])
        count +=1
        #iterate through all nodes in current level
        for i in  range(size):

            node = queue.popleft()
            #process current node
            if count % 2 == 0:
                current_lvl.append(node.data)
            else:
                current_lvl.appendleft(node.data)
            
             #add nodes in subsequent level to queue
            if node.l_child:
                queue.append(node.l_child)
            if node.r_child:
                queue.append(node.r_child)



        levels.append(current_lvl)
    
    return levels

bst = Node(5)
binary_insert(bst,Node(3))
binary_insert(bst,Node(8))
binary_insert(bst,Node(2))
binary_insert(bst,Node(4))
binary_insert(bst,Node(6))
binary_insert(bst,Node(7))
binary_insert(bst,Node(9))
binary_insert(bst,Node(10))

print(zig_zag_traversal(bst))
