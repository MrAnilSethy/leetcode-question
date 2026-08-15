class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sub = nums[0]
        min_sub = nums[0]
        maxsub_res = nums[0]
        minsub_res = nums[0]
        total=0
        for i in range(1,len(nums)):
            max_sub = max(max_sub+nums[i],nums[i])
            min_sub = min(min_sub+nums[i],nums[i])
            maxsub_res = max(maxsub_res,max_sub)
            minsub_res = min(minsub_res,min_sub)
            total+=nums[i]
        total+=nums[0]

        if maxsub_res < 0:
            return maxsub_res
        circular_sum = total-minsub_res
        return max(maxsub_res,circular_sum)
