class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            previous, current = current, previous
        
        return previous[0]