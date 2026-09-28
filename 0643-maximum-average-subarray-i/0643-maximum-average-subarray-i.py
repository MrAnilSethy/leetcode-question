class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0
        for i in range(k):
            curr_sum+=nums[i]
        max_sum = curr_sum
        low = 0
        high = k
        while(high<n):
            curr_sum-=nums[low]
            curr_sum+=nums[high]
            max_sum = max(curr_sum,max_sum)
            low+=1
            high+=1
        return max_sum/k