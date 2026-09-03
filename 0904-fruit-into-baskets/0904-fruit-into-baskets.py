class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low  = 0
        dic = {}
        res = -1
        for high in range(len(fruits)):
            dic[fruits[high]] = dic.get(fruits[high],0)+1
            while(len(dic)>2):
                dic[fruits[low]]-=1
                if dic[fruits[low]]==0:
                    del dic[fruits[low]]
                low+=1
            size = high-low+1
            res = max(size,res)
        return res
            



        