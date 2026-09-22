class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        end = len(s)-1
        while(st<=end):
            # skip the st side char is not alnum
            while(st<end and not s[st].isalnum()):
                st+=1
            # skip the right side char is not alnum
            while(st<end and not s[end].isalnum()):
                end-=1
            if s[st].lower()!=s[end].lower():
                return False
            st+=1
            end-=1
                
        return True

        