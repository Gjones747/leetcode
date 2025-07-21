# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #bfs

        if not root:
            return 0
        
        stack = deque([[root, 1]])

        while stack:
            curr = stack.pop()
            depth = curr[1]
            if not curr[0].right and not curr[0].left:
                return curr[1]
            
            if curr[0].right:
                stack.appendleft([curr[0].right, depth + 1])
            if curr[0].left:
                stack.appendleft([curr[0].left, depth + 1])