class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        res = -1
        freq = [0] * 256

        for high in range(len(s)):
            freq[ord(s[high])] += 1
            max_f = max(freq)
            size = high-low+1
            diff = size-max_f

            while diff> k:
                freq[ord(s[low])] -= 1
                low += 1
                max_f = max(freq)
                size = high-low+1
                diff = size-max_f

            res = max(res, high - low + 1)

        return res