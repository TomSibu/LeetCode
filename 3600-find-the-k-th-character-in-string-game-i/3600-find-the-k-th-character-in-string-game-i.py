class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        while len(word) < k:
            size = len(word)
            for i in range(size):
                next_letter = chr(ord('a') + ((ord(word[i]) - ord('a') + 1) % 26))
                word.append(next_letter)
        return word[k-1]