class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # sort the array
        nums.sort()
        max_sum = float('inf')
        ans = None
        n = len(nums)
        for i in range(n-2):
            left = i+1
            right = n-1
            while(left<right):
                sum = nums[i]+nums[left]+nums[right]
                diff = abs(sum-target)
                if diff<max_sum:
                    max_sum = diff
                    ans = sum
                # best case
                if sum==target:
                    return sum
                elif sum<target:
                    left+=1
                else:
                    right-=1
        return ans

        