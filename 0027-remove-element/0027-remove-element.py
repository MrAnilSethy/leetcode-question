class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ans = 0
        low = 0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            else:
                nums[low]=nums[i]
                low+=1
                ans+=1
        return ans
        