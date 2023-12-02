class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i] is not '*':
                stack.append(s[i])
            if s[i] is '*':
                stack.pop()
        rStack=''.join(stack)
        return rStack
        