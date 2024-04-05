class Solution:
    def checkValidParenthesis(self, s: str) -> bool:
        parenthesisSoFar = []
        validParentheses = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in parenthesesSoFar.values():
                stack.append(char)
            elif char in parentheses_map:
                if not stack or stack[-1] != parentheses_map[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
