class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sub = nums[0]
        min_sub = nums[0]
        max_res = nums[0]
        min_res = nums[0]
        res = abs(nums[0])
        for i in range(1,len(nums)):
            max_sub = max(max_sub+nums[i],nums[i])
            min_sub = min(min_sub+nums[i],nums[i])
            max_res = max(max_res,max_sub)
            min_res = min(min_res,min_sub)
            max_abs = abs(max_res)
            min_abs = abs(min_res)
            res = max(res,max(max_abs,min_abs))
        return res
        