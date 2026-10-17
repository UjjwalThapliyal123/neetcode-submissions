class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total = []
        for num in nums:
            if num in total:
                return True
            total.append(num)
        return False