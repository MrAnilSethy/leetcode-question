class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        sum = 0
        min_len = float("inf")
        for right in range(len(nums)):
            sum+=nums[right]
            while(sum>=target):
                size = right-left+1
                min_len = min(size,min_len)
                sum-=nums[left]
                left+=1
        return 0 if min_len==float("inf") else min_len