# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # An empty node is a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Recursively validate:
            # - Left child must be less than current node's value (updates upper bound)
            # - Right child must be greater than current node's value (updates lower bound)
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        # Start with infinite range boundaries
        return validate(root, float('-inf'), float('inf'))