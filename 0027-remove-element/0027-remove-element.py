class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        st = 0
        low = 0
        high = len(nums)-1
        ans = 0
        while(low<=high):
            if nums[low]==val:
                low+=1
                continue
            else:
                nums[st],nums[low] = nums[low],nums[st]
                st+=1
                low+=1
                ans+=1
        return ans







        