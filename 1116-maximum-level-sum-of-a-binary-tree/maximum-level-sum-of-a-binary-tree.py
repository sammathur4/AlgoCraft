# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = deque()
        q.append(root)
        maxSum = float('-inf')
        level = 0
        maxLevel = 0

        while q:
            size = len(q)
            currSum = 0
            for i in range(size):
                node = q.popleft()
                currSum+=node.val

                if node.left:
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

            level+=1
            if currSum>maxSum:
                maxSum=currSum
                maxLevel = level
        return maxLevel
        