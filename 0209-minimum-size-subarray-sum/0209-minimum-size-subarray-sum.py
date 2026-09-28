class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        curr_sum = 0
        min_len = float("inf")
        for high in range(len(nums)):
            curr_sum+=nums[high]
            while(curr_sum>=target):
                size = high-low+1
                min_len = min(min_len,size)
                curr_sum-=nums[low]
                low+=1
        return 0 if min_len==float("inf") else min_len



        