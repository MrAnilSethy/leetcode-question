class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st = 0
        for end in range(len(nums)):
            if nums[end]!=0:
                nums[st],nums[end]=nums[end],nums[st]
                st+=1
                