class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def go(i):
            if i in seen:
                return 0
            seen.add(i)
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    go(j)
            return 1
        
        n = len(isConnected)
        res = 0
        seen = set()
        for i in range(n):
            res += go(i)
            
        return res