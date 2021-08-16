class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)
def search_bst(root, node):
    if not node:
        return None
    elif node.data == root.data:
        return root
    elif node.data < root.data:
        return search_bst(root.l_child, node)
    elif node.data > root.data:
        return search_bst(root.r_child, node)

    
def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child) 

# bst = Node(4)
# n1= Node(1)
# n2 = Node(2)
# n5 = Node(5)
# n4 = Node(4)
# binary_insert(bst,n1)
# binary_insert(bst,n2)
# binary_insert(bst,n5)
# binary_insert(bst,n4)
# in_order_print(bst)
# print("-----", search_bst(bst,Node(2)).data)
