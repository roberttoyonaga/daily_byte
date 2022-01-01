# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.k = -1
        self.answer = -1
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.util(root)
        return self.answer
    def util(self, root):
        if root is None:
            return

        self.util(root.left)
        self.k -= 1
        if self.k == 0:
            self.answer = root.val
            return
        self.util(root.right)