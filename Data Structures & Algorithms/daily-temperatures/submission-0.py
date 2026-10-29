from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores pairs of [temperature, index]
        
        for i, t in enumerate(temperatures):
            # While stack is not empty and current temperature is warmer than the top of the stack
            while stack and t > stack[-1][0]:
                stack_Temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            
            stack.append([t, i])
            
        return res