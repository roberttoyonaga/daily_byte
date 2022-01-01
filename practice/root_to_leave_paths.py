from BST import *

def root_to_leaf_paths(root):
    paths = []
    util(root,[], paths)
    return paths

def util(root,current_path, paths):
    current_path_2 = list(current_path) # need to copy list (do NOT need deep copy though bc only one dimension)
    current_path_2.append(root.data)

    if not root.l_child and not root.r_child: # if both children are null
        paths.append(current_path_2)
        return
        
    if root.l_child:
        util(root.l_child, current_path_2, paths)
    if root.r_child:
        util(root.r_child, current_path_2, paths)


bst = Node(5)
binary_insert(bst,Node(3))
binary_insert(bst,Node(7))
binary_insert(bst,Node(4))
binary_insert(bst,Node(6))
binary_insert(bst,Node(1))
binary_insert(bst,Node(8))
binary_insert(bst,Node(2))

print(root_to_leaf_paths(bst))