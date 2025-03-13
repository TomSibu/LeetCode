class Solution:
    def reverse(self, x: int) -> int:
        a=int(str(abs(x))[::-1])
        if x<0:
            a=-a
        if a < -2 ** 31 or a > 2 ** 31 - 1:
            return 0
        return a