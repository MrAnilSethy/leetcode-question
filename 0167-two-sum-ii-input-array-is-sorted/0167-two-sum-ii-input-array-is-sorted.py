class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        st = 0
        end = len(numbers)-1
        while(st<end):
            sum = numbers[st]+numbers[end]
            if sum==target:
                return [st+1,end+1]
            elif sum<target:
                st+=1
            else:
                end-=1

        return -1