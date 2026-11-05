class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up position and speed, then sort by position in descending order 
        # (closest to the target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            # Calculate time needed to reach the target
            time = (target - pos) / spd
            
            # If stack is not empty and the current car takes less than or equal 
            # time compared to the car ahead of it, it catches up and joins that fleet.
            if stack and time <= stack[-1]:
                continue
            
            # Otherwise, it forms a new fleet.
            stack.append(time)
            
        return len(stack)