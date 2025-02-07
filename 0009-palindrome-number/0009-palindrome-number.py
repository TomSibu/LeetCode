class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = a[::-1]
        if b == a:
            return True
        else:
            return False