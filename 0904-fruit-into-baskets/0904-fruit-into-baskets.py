class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low = 0
        dic = {}
        max_fruits = float("-inf")
        for high in range(len(fruits)):
            dic[fruits[high]] = dic.get(fruits[high],0)+1
            if len(dic)>2:
                dic[fruits[low]]-=1
                if dic[fruits[low]]==0:
                    del dic[fruits[low]]
                low+=1
            size = high-low+1
            max_fruits = max(max_fruits,size)
        return max_fruits


        