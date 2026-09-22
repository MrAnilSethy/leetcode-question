class Solution:
    def maxArea(self, height: list[int]) -> int:
        st = 0
        end = len(height)-1
        max_water = 0
        while(st<end):
            width = end-st
            curr_water = min(height[st],height[end])*width
            max_water = max(max_water,curr_water)
            if height[st]<height[end]:
                st+=1
            else:
                end-=1
        return max_water