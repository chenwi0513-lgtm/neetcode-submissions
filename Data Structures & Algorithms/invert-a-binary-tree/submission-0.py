# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            leftTree = self.invertTree(root.left)
            rightTree = self.invertTree(root.right)
            if leftTree or rightTree:
                root.right, root.left = leftTree, rightTree
        return root