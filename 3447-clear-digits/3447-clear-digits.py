class Solution:
    def clearDigits(self, s: str) -> str:
        chars = list(s)
        to_remove = set()
        
        for i, ch in enumerate(chars):
            if ch.isdigit():
                to_remove.add(i)
                for j in range(i - 1, -1, -1):
                    if chars[j].isalpha() and j not in to_remove:
                        to_remove.add(j)
                        break  
        
        result = "".join([chars[i] for i in range(len(chars)) if i not in to_remove])
        return result