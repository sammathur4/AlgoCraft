# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        def travel(node, val):
            nonlocal res
            if node.val == val:
                res = node
                return
            if node.left:
                travel(node.left, val)
            if node.right:
                travel(node.right, val)

        res = None
        travel(root, val)

        return res
        