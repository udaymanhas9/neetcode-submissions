# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0


        def dfs(node, cnt):
            if not node:
                self.max_length = max(self.max_length, cnt)
                return
            
            dfs(node.left, cnt+1)
            dfs(node.right, cnt +1)
        
        dfs(root, 0)

        return self.max_length