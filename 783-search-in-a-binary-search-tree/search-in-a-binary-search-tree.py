# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def run(root):
            if root.val==val:return root

            if root.left:
                left_ans = run(root.left)
                if left_ans:
                    return left_ans
            if root.right:
                right_ans = run(root.right)
                if right_ans:
                    return right_ans

            return None
        return run(root)
        