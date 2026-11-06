# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # Pop the smallest element
            curr = stack.pop()
            k -= 1
            
            # If k reaches 0, we've found the kth smallest element
            if k == 0:
                return curr.val
                
            # Visit the right subtree
            curr = curr.right