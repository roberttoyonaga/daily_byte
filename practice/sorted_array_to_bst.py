from BST import *

def sorted_array_to_bst(arr):
    return build_tree(0, len(arr)-1, arr)
    

def build_tree(left, right, arr):

    #leaves
    if left > right:
        return None
    
    # not leaves
    mid = left + (right - left)//2  #floor division   
    root = Node(arr[mid])

    root.l_child = build_tree(left, mid -1, arr) #
    root.r_child = build_tree(mid+1, right, arr)
    return root

arr = [1,2,3,4,5,6,7,8,9]
bst = sorted_array_to_bst(arr)
in_order_print(bst)