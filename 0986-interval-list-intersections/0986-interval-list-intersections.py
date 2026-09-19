class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        res = []
        i = 0
        j = 0
        m = len(firstList)
        n = len(secondList)
        while(i<m and j<n):
            st1 = firstList[i][0]
            end1 = firstList[i][1]
            st2 = secondList[j][0]
            end2 = secondList[j][1]
            if(st1<=st2):
                # check intersection
                if(end1>=st2):
                    s = max(st1,st2)
                    e = min(end1,end2)
                    res.append([s,e])
            else:
                if(end2>=st1):
                    s = max(st1,st2)
                    e = min(end1,end2)
                    res.append([s,e])
            if (end1<=end2):
                i+=1
            else:
                j+=1
        return res

        