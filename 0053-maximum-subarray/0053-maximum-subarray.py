class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end = float('-inf')
        ans = nums[0]
        for i in range(len(nums)):
            v1 = end+nums[i]
            v2 = nums[i]
            end = max(v1,v2)
            ans = max(ans,end)
        return ans
        