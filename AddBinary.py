class Solution:
    def addBinary(self, a: str, b: str) -> str:
         x=bin(add(int(a,2),int(b,2)))
         return x[2:]