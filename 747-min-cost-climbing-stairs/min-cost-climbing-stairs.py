class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        1 2 3 stair
        '''
        
        memo = {0:0,1:0}
        '''
        def dfs(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 0
            memo[n] = min(dfs(n - 2) + cost[n - 2], dfs(n-1) + cost[n - 1]) 
            return memo[n]
        return dfs(len(cost))
        '''
        if len(cost) <= 1:
            return 0
        for i in range(2, len(cost) + 1):
            memo[i] = min(memo[i - 2] + cost[i - 2], memo[i - 1] + cost[i - 1])
        return memo[len(cost)]