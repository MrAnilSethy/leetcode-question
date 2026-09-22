class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dic = {}
        st = 0
        mid = 0
        end = len(nums) - 1

        while mid <= end:
            dic[nums[mid]] = dic.get(nums[mid], 0) + 1

            if dic[nums[mid]] > 2:
                mid += 1
                continue

            nums[st] = nums[mid]
            st += 1
            mid += 1

        return st