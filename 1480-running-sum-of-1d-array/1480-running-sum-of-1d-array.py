class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            running_sum.append(sum)
        return running_sum

        