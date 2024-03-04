# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(r, t, include):
            if r is None: return 0

            count = 0
            if r.val==t: count+=1

            count+=dfs(r.left, t-r.val, True) + dfs(r.right, t-r.val, True)
            if not include:
                count+=dfs(r.left, t, False) + dfs(r.right, t, False)
            return count
        
        return dfs(root, targetSum, False)



        