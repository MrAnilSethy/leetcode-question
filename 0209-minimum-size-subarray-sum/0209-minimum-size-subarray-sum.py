class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        sum = 0
        n = len(nums)
        res = float('inf')
        #hiring
        while(high<n):
            sum+=nums[high]
            #check target == sum
            while(sum>=target):
                sb = (high-low)+1
                res = min(sb,res)
                #firing
                sum-=nums[low]
                low+=1
            high+=1
       
        return 0 if res == float('inf') else res

                

        