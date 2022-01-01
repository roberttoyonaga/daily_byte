# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # halting conditions
        if not preorder and not inorder:
            return
        
        #current data
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) #find index of root in inorder arr
        
        #recurse
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        #return a value
        return root
    
        