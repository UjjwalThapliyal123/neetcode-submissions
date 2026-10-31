# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function returns [is_balanced, height]
        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # A tree is balanced if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. Height difference between left and right is <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            height = 1 + max(left[1], right[1])
            
            return [balanced, height]
        
        return dfs(root)[0]