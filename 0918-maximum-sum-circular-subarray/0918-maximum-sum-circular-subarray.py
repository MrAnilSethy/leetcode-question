class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sub = nums[0]
        min_sub = nums[0]
        max_res = nums[0]
        min_res = nums[0]
        total = 0
        for i in range(1,len(nums)):
            max_sub = max(max_sub+nums[i],nums[i])
            min_sub = min(min_sub+nums[i],nums[i])
            max_res = max(max_res,max_sub)
            min_res = min(min_res,min_sub)
            total+=nums[i]
        total+=nums[0]

        if max_res<0:
            return max_res
        circular_res = total-min_res
        return max(circular_res,max_res)
        