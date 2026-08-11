class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = []
        nev = []
        for num in nums:
            if num<0:
                nev.append(num)
            else:
                pos.append(num)
        if len(nev) == 0:
            return [x*x for x in pos]
        elif len(pos) == 0:
            return [x*x for x in nev][::-1]
        else:
            pos = [x*x for x in pos]
            nev = [x*x for x in nev][::-1]
            i = 0
            j = 0
            m = len(pos)
            n = len(nev)
            res = []
            while(i<m and j<n):
                if(pos[i]<nev[j]):
                    res.append(pos[i])
                    i+=1
                else:
                    res.append(nev[j])
                    j+=1
            while(i<m):
                res.append(pos[i])
                i+=1
            while(j<n):
                res.append(nev[j])
                j+=1
        return res
            

        