class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        res = 0
        freq = [0] * 256

        for high in range(len(s)):
            freq[ord(s[high])] += 1

            while (high - low + 1) - max(freq) > k:
                freq[ord(s[low])] -= 1
                low += 1

            res = max(res, high - low + 1)

        return res