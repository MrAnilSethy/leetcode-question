class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minend = nums[0]
        maxend = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            v1 = minend * nums[i]
            v2 = maxend * nums[i]
            v3 = nums[i]
            minend = min(v1,min(v2,v3))
            maxend = max(v1,max(v2,v3))
            res = max(res,max(minend,maxend))
        return res

        