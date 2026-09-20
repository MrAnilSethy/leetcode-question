class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0,n-2):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            s = -1 * nums[i]
            left = i+1
            right = n-1
            while(left<right):
                sum = nums[left]+nums[right]
                if sum==s:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    # left side duplicate
                    while(left<n and nums[left]==nums[left-1]):
                        left+=1
                    # right side duplicate
                    while(right>=0 and nums[right]==nums[right+1]):
                        right-=1
                elif sum<s:
                    left+=1
                else:
                    right-=1
        return res

        