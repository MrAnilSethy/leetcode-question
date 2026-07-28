class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        sum = 0
        n = len(nums)
        res = float('inf')
        for high in range(n):
            sum+=nums[high]

            while sum >= target:
                res = min(res,high-low+1)
                sum-=nums[low]
                low+=1
        return 0 if res == float('inf') else res
        