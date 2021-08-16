from BST import *

'''
Method 1: Get all nodes (or a pointer to all nodes) put in a list.
Iterate through list setting right val of prev node to the next node in the list. 
This requres you to visit each node twice and also uses memory required to make the list of pointers
'''
def get_in_order(root, l):
    if not root:
        return
    get_in_order(root.l_child, l)
    l.append(root)
    get_in_order(root.r_child, l)

def flatten_bst(root):
    l=[]
    get_in_order(root, l)


    for i in range(len(l)):
        node = l[i]
        node.l_child = None
        if(i < len(l)-1):
            node.r_child = l[i+1]
    
    return l[0]
#---------------------------------------------------------
def print_flattened_bst(root):
    while root:
        print(root.data)
        root = root.r_child

bst = Node(4)
n1= Node(1)
n2 = Node(2)
n5 = Node(5)
n4 = Node(4)
binary_insert(bst,n1)
binary_insert(bst,n2)
binary_insert(bst,n5)
binary_insert(bst,n4)
flattened = flatten_bst(bst)
print_flattened_bst(flattened)
