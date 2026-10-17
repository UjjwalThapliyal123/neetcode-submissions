class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map [ iterate through the array once ,keeping the track of the both the current element value  and the indicies]
        # diff = targ - n 
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i