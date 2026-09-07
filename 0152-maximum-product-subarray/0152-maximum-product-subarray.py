class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nev_end = nums[0]
        pos_end = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            curr_index = nums[i]
            curr_nev = nev_end * nums[i]
            curr_pos = pos_end * nums[i]
            nev_end = min(curr_index,min(curr_nev,curr_pos))
            pos_end = max(curr_index,max(curr_nev,curr_pos))
            res = max(res,max(nev_end,pos_end))
        return res