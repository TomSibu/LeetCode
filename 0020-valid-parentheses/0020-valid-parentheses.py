class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in parenthesis_pair:
                if stack and stack[-1] == parenthesis_pair[char]:  
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) 
        
        return not stack 