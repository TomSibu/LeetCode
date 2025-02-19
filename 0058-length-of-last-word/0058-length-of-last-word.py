class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        word=words[-1]
        return len(word)