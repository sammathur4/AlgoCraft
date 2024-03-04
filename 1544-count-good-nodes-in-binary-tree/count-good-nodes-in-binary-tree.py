# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node, currMax):
            if not node: return 0

            if node.val>=currMax:
                count = 1
            else:
                count = 0
            
            currMax = max(currMax, node.val)
            count+=helper(node.left, currMax)
            count+=helper(node.right, currMax)
            return count
        
        return helper(root, root.val)

        