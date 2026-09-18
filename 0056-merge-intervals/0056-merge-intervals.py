class Solution:
    def merge(self, arr: list[list[int]]) -> list[list[int]]:
        arr.sort()
        res = []
        st1 = arr[0][0]
        end1 = arr[0][1]
        for i in range(1,len(arr)):
            st2 = arr[i][0]
            end2 = arr[i][1]
            if end1>=st2: # if merge
                st1 = st1
                end1 = max(end1,end2)
                continue
            # not merge
            res.append([st1,end1])
            st1 = st2
            end1 = end2
        res.append([st1,end1])
        return res
        