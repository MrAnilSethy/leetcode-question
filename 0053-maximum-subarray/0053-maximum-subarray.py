class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxend = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = maxend + nums[i]
            maxend = max(v1,v2)
            res = max(res,maxend)
        return res