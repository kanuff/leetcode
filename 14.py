
class Solution:
    # weirdly slow, don't really like the nested loop
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        strs.sort(key = len)
        base = strs[0]
        for i, char in enumerate(base):
            for word in strs:
                if word[i] != char:
                    return base[:i]
        return base            

