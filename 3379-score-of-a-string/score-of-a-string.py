class Solution:
    def scoreOfString(self, s: str) -> int:
        tots = 0

        for i in range(len(s) - 1):
            tots+= abs(ord(s[i]) - ord(s[i+1]))
        return tots
        