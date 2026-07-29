class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dic = {}
        res = 0
        for right,ch in enumerate(s):
            if ch in dic and dic[ch]>=left:
                left = dic[ch]+1
            dic[ch]=right
            res = max(res,right-left+1)
        return res
        