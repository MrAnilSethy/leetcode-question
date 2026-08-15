class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsub = nums[0]
        minsub = nums[0]
        maxsub_res = nums[0]
        minsub_res = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            maxsub = max(maxsub+nums[i],nums[i])
            minsub = min(minsub+nums[i],nums[i])
            maxsub_res = max(maxsub_res,maxsub)
            minsub_res = min(minsub_res,minsub)

            abs_maxsub = abs(maxsub_res)
            abs_minsub = abs(minsub_res)
            res = max(res,max(abs_maxsub,abs_minsub))
        return abs(res)
        
        