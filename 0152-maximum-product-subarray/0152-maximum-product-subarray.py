class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_end = nums[0]
        max_end = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            curr_index = nums[i]
            curr_min_end = min_end * nums[i]
            curr_max_end = max_end * nums[i]
            min_end = min(curr_index,min(curr_min_end,curr_max_end))
            max_end = max(curr_index,max(curr_min_end,curr_max_end))
            res = max(res,max(min_end,max_end))
        return res
        