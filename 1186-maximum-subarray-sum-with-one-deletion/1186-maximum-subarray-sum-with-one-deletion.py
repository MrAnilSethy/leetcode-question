class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodel = arr[0]
        onedel = float('-inf')
        res = arr[0]

        for i in range(1, len(arr)):
            prevnodel = nodel
            prevonedel = onedel

            # Don't delete anything
            nodel = max(prevnodel + arr[i], arr[i])

            # Either:
            # 1. Delete arr[i]
            # 2. We already deleted something earlier
            onedel = max(prevnodel, prevonedel + arr[i])

            res = max(res, nodel, onedel)

        return res