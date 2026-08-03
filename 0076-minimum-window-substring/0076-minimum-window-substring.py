class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low = 0
        res = float('inf')
        freq = [0]*256
        nedded = [0]*256
        start = 0
        def check(freq,nedded):
            for i in range(256):
                if freq[i]<nedded[i]:
                    return False
            return True
        for ch in t:
            nedded[ord(ch)]+=1
        for high in range(len(s)):
            freq[ord(s[high])]+=1

            while(check(freq,nedded)):
                size = high-low+1
                if res>size:
                    res = size
                    start = low
                freq[ord(s[low])]-=1
                low+=1
        return "" if res == float('inf') else s[start:start+res]

        

        