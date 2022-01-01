from BST import *

def identical_trees(root1, root2):
    #take care of stopping conditions
    if (root1 and not root2) or (root2 and not root1):
        return False
    elif not root1 and not root2:
        return True
    elif root1.data != root2.data:
        return False
        
    # recurse on left and right subtrees making sure everythign is the same
    else:
        return identical_trees(root1.l_child, root2.l_child) and identical_trees(root1.r_child, root2.r_child) 


n1= Node(1)
n2 = Node(2)
n5 = Node(5)
n9 = Node(9)
bst = Node(7)
binary_insert(bst,n2)
binary_insert(bst,n9)
binary_insert(bst,n1)
binary_insert(bst,n5)

n1_2= Node(1)
n2_2 = Node(2)
n5_2 = Node(5)
n9_2 = Node(9)
bst_2 = Node(7)
binary_insert(bst_2,n2_2)
binary_insert(bst_2,n9_2)
binary_insert(bst_2,n1_2)
binary_insert(bst_2,n5_2)
print(identical_trees(bst, bst_2))
