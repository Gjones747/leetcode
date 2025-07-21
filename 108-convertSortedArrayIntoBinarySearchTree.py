# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not len(nums):
            return None
        
        middleNode = nums//2

        return TreeNode(
            nums[middleNode],
            self.sortedArrayToBST(nums[:middleNode]),
            self.sortedArrayToBST(nums[middleNode+1:])
        )


