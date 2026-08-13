class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxend = nums[0]
        minend = nums[0]

        res = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = maxend * nums[i]
            v3 = minend * nums[i]
            maxend = max(v1,max(v2,v3))
            minend = min(v1,min(v2,v3))
            res = max(res,max(maxend,minend))
        return res
        