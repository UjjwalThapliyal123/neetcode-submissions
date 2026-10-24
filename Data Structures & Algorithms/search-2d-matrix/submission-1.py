class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        
        # Step 1: Find the potential row using binary search
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
                
        if not (top <= bot):
            return False
            
        row = (top + bot) // 2
        
        # Step 2: Perform binary search within the identified row
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True       # <--- Fixed: return True immediately
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return False