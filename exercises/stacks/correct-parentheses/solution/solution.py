class Solution:
    def isCorrect(self, s: str) -> bool:
        print(f"Provided string: {s}")
        stack = []
        parentheses_map = {")":"(", "}":"{", "]":"["} #pairs of characters that represent valid parentheses
        
        for char in s: #iterate through every character in string of parentheses
            print(f"Evaluating char {char} with stack {stack}")
            if char in parentheses_map.values(): #if opening parentheses, add to stack to check again for closing
                stack.append(char) #add to stack
            elif char in parentheses_map: #if character is a closing parentheses
                if not stack or stack[-1] != parentheses_map[char]: #and there is not a corresponding opening parentheses
                    print(f"Not valid parentheses! (1)")
                    return False #then the string provided does not contain valid parentheses
                stack.pop() #otherwise remove the valid parentheses from the stack
            else: #if contains some other character that is not parentheses, fails
                print(f"Not valid parentheses! (2)")
                return False
        
        return not stack #if stack is empty, these are valid parentheses
