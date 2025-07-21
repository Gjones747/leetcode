# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): 
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        total_tilt = 0

        def totalNode(node):
            nonlocal total_tilt
            if not node:
                return 0

            totalLeft = totalNode(node.right)
            totalRight = totalNode(node.left)
            tilt = abs(totalLeft - totalRight)
            total_tilt += tilt

            return node.val + totalLeft + totalRight

        totalNode(root)

        return total_tilt
        