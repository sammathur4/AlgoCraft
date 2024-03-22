class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temps)
        
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        
        return ans