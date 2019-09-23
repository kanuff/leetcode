class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        open = -1
        res = ""
        for i in range(len(S)):
            if S[i] == "(":
                if open >= 0:
                    res += S[i]
                open += 1
            elif S[i] == ")":
                if open > 0:
                    res += S[i]
                open -= 1
        return res

                    