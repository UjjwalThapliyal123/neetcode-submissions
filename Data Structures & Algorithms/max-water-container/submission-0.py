class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max_areas = 0

        while l<r:
            width = r - l 
            current_area = width * min(heights[l],heights[r])
            max_areas = max(max_areas,current_area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_areas
