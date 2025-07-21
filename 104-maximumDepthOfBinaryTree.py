# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 

# bfs iteration
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         # going to use bfs 
#         if root:
#             depth = 1
#             stack = deque([[root, depth]])
#         else:
#             return 0
#         while stack:
#             current = stack.pop()
#             print(current)
#             depth = current[1]
#             if current[0].right:
#                 stack.appendleft([current[0].right, depth+1])
#             if current[0].left:
#                 stack.appendleft([current[0].left, depth+1])
#         return depth

# dfs recursion
class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))