class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        st = 0
        mid = 0
        end = len(nums)-1
        while(mid<=end):
            if st<2 or nums[mid]!=nums[st-2]:
                nums[st]=nums[mid]
                st+=1
                mid+=1
            else:
                mid+=1
                continue
        return st