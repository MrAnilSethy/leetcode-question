class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,num in enumerate(nums):
            nedded = target-num

            if nedded in dic:
                return [dic[nedded],i]
            dic[num] = i


        