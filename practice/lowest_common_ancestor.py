from BST import *

'''bst must be balanced'''
def lowest_common_ancestor(root,a, b):
    if root.data < a and root.data < b:
        return lowest_common_ancestor(root.r_child, a, b)
    elif root.data > a and root.data > b:
        return lowest_common_ancestor(root.l_child, a, b)
    else:
        return root.data

# balanced
n1= Node(1)
n2 = Node(2)
n5 = Node(5)
n9 = Node(9)
bst = Node(7)
binary_insert(bst,n2)
binary_insert(bst,n9)
binary_insert(bst,n1)
binary_insert(bst,n5)

# unbalanced doesnt work
# n1= Node(1)
# n2 = Node(2)
# n5 = Node(5)
# n7 = Node(7)
# bst = Node(4)
# binary_insert(bst,n1)
# binary_insert(bst,n7)
# binary_insert(bst,n2)
# binary_insert(bst,n5)

print(lowest_common_ancestor(bst,1, 5))