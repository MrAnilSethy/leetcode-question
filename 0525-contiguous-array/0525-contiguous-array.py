class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        mp = {}
        res = 0
        zero = 0
        one = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one

            if diff == 0:
                res = max(res, i + 1)

            elif diff not in mp:
                mp[diff] = i

            else:
                indx = mp[diff]
                size = i - indx
                res = max(res, size)

        return res