class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        count = 0
        map = {}
        map[0] = 1
        for i in range(len(nums)):
            curr_sum+=nums[i]
            ques = curr_sum-k
            freq = map.get(ques,0)
            count+=freq
            map[curr_sum] = map.get(curr_sum,0)+1
        return count