class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        sum = 0
        res = float("inf")
        n = len(nums)
        while(high<n):
            sum+=nums[high]
            while(sum>=target):
                size = high-low+1
                res = min(res,size)
                sum-=nums[low]
                low+=1
            high+=1
        return 0 if res==float("inf") else res

        