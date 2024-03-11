class Solution:
    def dfs(self, adj, visited, minChange, currCity):
        visited[currCity] = True
        for neighbour in adj[currCity]:
            if not visited[neighbour[0]]:
                if neighbour[1] == 1:
                    minChange[0]+=1
                self.dfs(adj, visited, minChange, neighbour[0])
        
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for con in connections:
            adj[con[0]].append((con[1], 1))
            adj[con[1]].append((con[0], -1))

        visited = [False]*n
        minChange = [0]
        self.dfs(adj, visited, minChange, 0)

        return minChange[0]


        