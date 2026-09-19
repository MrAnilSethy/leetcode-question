class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        st1 = intervals[0][0]
        end1 = intervals[0][1]
        res = []
        for i in range(1,len(intervals)):
            st2 = intervals[i][0]
            end2 = intervals[i][1]
            # check ovverlap
            if end1>=st2:
                st1 = st1
                end1 = max(end1,end2)
                continue
            else:
                res.append([st1,end1])
                st1 = st2
                end1 = end2
        res.append([st1,end1])
        return res



        