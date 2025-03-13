class Solution:
    def reverse(self, x: int) -> int:
        t=abs(x)
        a=int(str(t)[::-1])
        if x<0:
            a=-a
        if (-2)**31 <= a <= (2**31)-1:
            return a
        return 0