class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        st = 0

        for mid in range(len(nums)):
            if st < 2 or nums[mid] != nums[st - 2]:
                nums[st] = nums[mid]
                st += 1

        return st