class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # create 3 variable i->fixed st and end varibale
        n = len(nums)
        res = []
        for i in range(n-2): #the goes to 0 to n-2 becase 2 place for left and right
            # check the "i" side duplicate
            if(i>0 and nums[i]==nums[i-1]):
                continue
            s = -1*nums[i]
            st = i+1
            end = n-1
            while(st<end):
                sum = nums[st]+nums[end]
                if sum==s:
                    res.append([nums[i],nums[st],nums[end]])
                    st+=1
                    end-=1

                    # check the st side duplicate
                    while(st<end and nums[st]==nums[st-1]):
                        st+=1
                    # check the end side duplicate
                    while(end>0 and nums[end]==nums[end+1]):
                        end-=1
                elif sum<s:
                    st+=1
                else:
                    end-=1
        return res
