# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # A node is "good" if its value is greater than or equal to the maximum value seen so far on this path
            good = 1 if node.val >= max_val else 0
            
            # Update the max value along the current path
            new_max = max(max_val, node.val)
            
            # Recursively count good nodes in left and right subtrees
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            
            return good

        return dfs(root, root.val)