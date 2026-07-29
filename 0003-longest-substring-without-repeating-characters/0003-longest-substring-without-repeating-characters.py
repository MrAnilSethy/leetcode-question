class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_index = {}
        res = 0
        for right,ch in enumerate(s):
            if ch in last_index and last_index[ch]>=left:
                left = last_index[ch]+1
            last_index[ch] = right
            res = max(res,right-left+1)
        return res

        