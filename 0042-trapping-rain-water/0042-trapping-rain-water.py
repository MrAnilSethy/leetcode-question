class Solution:
    def trap(self, height: list[int]) -> int:
        trapped_water = 0
        width = 1
        n = len(height)
        # left side max water
        leftmax = [0]*n
        leftmax[0]=height[0]
        for i in range(n):
            leftmax[i]=max(height[i],leftmax[i-1])

        # right side max water
        rightmax = [0]*n
        rightmax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i]=max(height[i],rightmax[i+1])
        
        for i in  range(n):
            water_level = min(leftmax[i],rightmax[i])
            trapped_water+=(water_level-height[i])*width
        return trapped_water
        

        
        