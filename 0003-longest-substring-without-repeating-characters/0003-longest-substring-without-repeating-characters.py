class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dic = {}
        res = 0

        for right,ch in enumerate(s):
            # check the ch already inn dic
            if ch in dic and dic[ch]>=left:
                left = dic[ch]+1
            dic[ch]=right
            size = right-left+1
            res = max(size,res)
        return res


        