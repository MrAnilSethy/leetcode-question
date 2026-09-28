class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        dic = {}
        max_len = 0
        for high,ch in enumerate(s):
            if ch in dic and dic[ch]>=low:
                low = dic[ch]+1
            dic[ch] = high
            size = high-low+1
            max_len = max(max_len,size)
        return max_len



        