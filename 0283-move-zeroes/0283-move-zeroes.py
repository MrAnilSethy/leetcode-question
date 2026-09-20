class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        for high in range(len(nums)):
            if nums[high]!=0:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
     