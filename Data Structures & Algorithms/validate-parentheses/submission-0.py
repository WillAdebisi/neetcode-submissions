class Solution:
    def isValid(self, s: str) -> bool:
        op = "{[("  
        stack = []
        for char in s:
            if char in op:
                stack.append(char)
            else:
                if char == '}':
                    if not stack or stack.pop() != "{":
                        return False
                if char == ']':
                    if not stack or stack.pop() != "[":
                        return False
                if char == ')':
                    if not stack or stack.pop() != "(":
                        return False
        
        return len(stack) == 0
                




        