from BST import *

def calculate_depth(root):
    return util(root,0)

def util(root, depth):
    if root == None:
        return depth
    return max(util(root.l_child, depth+1),util(root.r_child, depth+1))


bst = Node(4)
n1= Node(1)
n2 = Node(2)
n5 = Node(5)
n4 = Node(6)
n0 = Node(0)
n7 = Node(7)
binary_insert(bst,n1)
binary_insert(bst,n2)
binary_insert(bst,n5)
binary_insert(bst,n4)
binary_insert(bst,n0)
binary_insert(bst,n7)

print(calculate_depth(bst))