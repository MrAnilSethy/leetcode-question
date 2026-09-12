class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        map = {}
        count = 0
        map[0] = 1
        for i in range(len(nums)):
            sum+=nums[i]
            rem = sum % k
            if rem<0:
                rem+=k
            freq = map.get(rem,0)
            count+=freq
            map[rem] = map.get(rem,0)+1
        return count
        