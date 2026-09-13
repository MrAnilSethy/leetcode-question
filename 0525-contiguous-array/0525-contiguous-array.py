class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        zero = 0
        one = 0
        map = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
            else:
                one+=1
            diff = zero-one
            if diff==0:
                res = max(res,i+1)
            elif diff not in map:
                map[diff] = i
            else:
                indx = map.get(diff,0)
                leng = i - indx
                res = max(res,leng)
        return res
        