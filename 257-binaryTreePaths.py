# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        stack = []
        stack.append(root)
        visited = []
        stringToAdd = ""

        final = []

        while len(stack) > 0:
            print(stringToAdd)
            stringToAdd = stringToAdd + str(stack[0].val) + "->"
            if stack[0].left and stack[0].left not in visited:
                stack.insert(1, (stack[0].left))
            if stack[0].right and stack[0].right not in visited:
                stack.insert(1,(stack[0].right))
                

            if not stack[0].right and not stack[0].left:
                final.append(stringToAdd[:-2])
                visited = []
                stringToAdd = ""
            visited.append(stack[0])

            stack.pop(0)

        print(final)
        return final
            
