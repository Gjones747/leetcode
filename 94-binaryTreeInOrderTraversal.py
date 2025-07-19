# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def recurse(self, root, answer):
        if not root:
            return answer
        
        self.recurse(root.left, answer)
        answer.append(root.val)
        self.recurse(root.right, answer)
        return answer

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = []
        return self.recurse(root, answer)
        

