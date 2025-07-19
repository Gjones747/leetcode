# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        print(root.val)

        if root.right:
            if root.val != root.right.val:
                return False
        if root.left:
            if root.val != root.left.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right) 