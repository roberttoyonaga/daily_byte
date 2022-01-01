from collections import deque
from BST import *

'''
this one seems weird, but its really similar to gather_levels because you need a BFS. 
All you gotta do is only add the first val at each level
'''
def visible_values(root):
    queue = deque([root])
    levels = []

    while queue:
        size = len(queue) # amount of nodes in current level
        current_lvl = []
        
        #iterate through all nodes in current level
        for i in  range(size):

            #process current node
            node = queue.popleft()

            # only return the first (left-most) value in each level. It is the only ont the is visible
            if i == 0:
                current_lvl.append(node.data)

            #add nodes in subsequent level to queue
            if node.l_child:
                queue.append(node.l_child)
            if node.r_child:
                queue.append(node.r_child)
        levels.append(current_lvl)
    
    return levels

bst = Node(4)
n1= Node(1)
n2 = Node(2)
n5 = Node(5)
n4 = Node(6)
n0 = Node(0)
n9 = Node(9)
n19 = Node(19)

binary_insert(bst,n1)
binary_insert(bst,n2)
binary_insert(bst,n5)
binary_insert(bst,n4)
binary_insert(bst,n0)
binary_insert(bst,n9)
binary_insert(bst,n19)

print(visible_values(bst))
