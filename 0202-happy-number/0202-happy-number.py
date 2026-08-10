class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        def fun(n):
            sum = 0
            while(n>0):
                d = n%10
                n = n//10
                sum+=d*d
            return sum
        while(fast!=1):
            slow = fun(slow)
            fast = fun(fast)
            fast = fun(fast)
            if(slow==fast and fast!=1):
                return False
        return True
        