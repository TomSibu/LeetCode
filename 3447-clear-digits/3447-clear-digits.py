class Solution:
    def clearDigits(self, s: str) -> str:
        s1=''
        for i in s:
            if i.isalpha():
                s1+=i
            else:
                s1=s1[:-1]
        return s1