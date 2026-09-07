class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestending = nums[0]
        sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum = bestending+nums[i]
            curr_index = nums[i]
            bestending = max(curr_sum,curr_index)
            sum = max(bestending,sum)
        return sum
        