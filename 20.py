class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        match = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        for symbol in s:
            if len(stack) == 0:
                stack.append(symbol)
            elif stack[-1] == match[symbol]:
                stack.pop()
            else:
                stack.append(symbol)
        return len(stack) == 0
            
        