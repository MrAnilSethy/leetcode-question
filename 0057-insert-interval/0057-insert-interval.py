class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.sort()
        insert = False
        res = []
        for i in range(len(intervals)):
            st = intervals[i][0]
            if st>=newInterval[0] and insert==False:
                res.append(newInterval)
                insert=True
            res.append(intervals[i])
        if insert==False:
            res.append(newInterval)
        # after insert check overlapping
        res.sort()
        st1 = res[0][0]
        end1 = res[0][1]
        ans = []
        for i in range(1,len(res)):
            st2 = res[i][0]
            end2 = res[i][1]
            if end1>=st2:
                st1 = st1
                end1 = max(end1,end2)
                continue
            # not overlaap
            ans.append([st1,end1])
            st1 = st2
            end1 = end2
        ans.append([st1,end1])
        return ans


        