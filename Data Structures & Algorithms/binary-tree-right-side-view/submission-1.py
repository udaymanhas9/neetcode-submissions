# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        _dic = defaultdict(list)

        def dfs(node, cnt):
            if not node:
                return

            _dic[cnt].append(node.val)

            dfs(node.left, cnt+1)
            dfs(node.right, cnt +1)
        
        dfs(root, 0)
        return [lst[-1] for lst in _dic.values()]