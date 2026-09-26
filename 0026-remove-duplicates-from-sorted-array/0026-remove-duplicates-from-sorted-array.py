class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        st = 0
        mid = 1
        end = len(nums)-1
        count = 1
        while(mid<=end):
            if nums[mid]==nums[mid-1]:
                mid+=1
                continue
            else:
                nums[st+1]=nums[mid]
                st+=1
                count+=1
                mid+=1
        return count
        