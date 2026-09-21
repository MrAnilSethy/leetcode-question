class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        low = 0
        st = 1
        end = len(nums)-1
        res = 1
        while(st<=end):
            if nums[st]==nums[st-1]:
                st+=1
                continue
            else:
                nums[low+1]=nums[st]
                low+=1
                st+=1
                res+=1
        return res