class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        map = {}
        count = 0
        map[0] = 1
        for i in range(len(nums)):
            sum+=nums[i]
            ques = sum-k
            freq = map.get(ques,0)
            count+=freq
            map[sum] = map.get(sum,0)+1
        return count        