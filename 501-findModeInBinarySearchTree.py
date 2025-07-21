# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        keyList = {}

        def iterateTree(node):
            nonlocal keyList
            if not node:
                return 

            if node.val in keyList:
                keyList[node.val] += 1
            else:
                keyList[node.val] = 1
            
            return iterateTree(node.right), iterateTree(node.left)
        iterateTree(root)
        max = []
        maxVal = 0
        print(keyList)
        for key, value in keyList.items():
            if value == maxVal:
                max.append(key)
            if value > maxVal:
                maxVal = value
                max = []
                max.append(key)
            
        return max

        