class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1
        n = len(nums)-1
        res = 1
        while(j<=n):
            if nums[j]==nums[j-1]:
                j+=1
                continue
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
                res+=1
        return res
        