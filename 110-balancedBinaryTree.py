# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def checkSide(self, root):
        
        if not root:
            return 0, True
        else:
            leftHeight, left = self.checkSide(root.left)
            rightHeight, right = self.checkSide(root.right)
            return 1 + max(leftHeight,rightHeight), left and right and abs(leftHeight-rightHeight) <= 1


    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        final, truthy = self.checkSide(root)
        return truthy