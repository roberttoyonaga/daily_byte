from BST import *
from collections import deque

def column_order_traversal(root):
    columns = {}
    queue = deque([root])
    columnQueue = deque([0]) # -2 -1 0 1 2

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            column = columnQueue.popleft()
            columns.setdefault(column, []).append(node.data) #will create listif not exists

            if node.l_child:
                queue.append(node.l_child)
                columnQueue.append(column-1)
            if node.r_child:
                queue.append(node.r_child)
                columnQueue.append(column+1)
    ret = []
    for column in columns:
        ret.append(columns[column])

    return ret

bst = Node(5)
binary_insert(bst,Node(3))
binary_insert(bst,Node(7))
binary_insert(bst,Node(4))
binary_insert(bst,Node(6))
binary_insert(bst,Node(1))
binary_insert(bst,Node(8))
binary_insert(bst,Node(2))


print(column_order_traversal(bst)) #correct
