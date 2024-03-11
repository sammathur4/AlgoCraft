class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)

        def dfs(i):
            isConnected[i][i] = 2

            for j in range(0, n):
                if isConnected[i][j] == 1:
                    isConnected[i][j]=2

                    dfs(j)
            
        for i in range(0, n):
            if isConnected[i][i] == 1:
                res+=1
                dfs(i)
        return res

        