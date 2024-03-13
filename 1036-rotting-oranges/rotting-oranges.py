class Solution:
    def dfs(self, rotten_after, grid, row, col):
        if (col < len(grid[0]) - 1 and grid[row][col + 1] == 1):
            if (rotten_after[row][col + 1] == 0 or rotten_after[row][col + 1] > rotten_after[row][col] + 1):
                rotten_after[row][col + 1] = rotten_after[row][col] + 1
                self.dfs(rotten_after, grid, row, col+1)
                
        if (col > 0 and grid[row][col - 1] == 1):
            if (rotten_after[row][col - 1] == 0 or rotten_after[row][col - 1] > rotten_after[row][col] + 1):
                rotten_after[row][col - 1] = rotten_after[row][col] + 1
                self.dfs(rotten_after, grid, row, col-1)
            
        if (row < len(grid) - 1 and grid[row + 1][col] == 1):
            if (rotten_after[row + 1][col] == 0 or rotten_after[row + 1][col] > rotten_after[row][col] + 1):
                rotten_after[row + 1][col] = rotten_after[row][col] + 1
                self.dfs(rotten_after, grid, row+1, col)
            
        if (row > 0 and grid[row - 1][col] == 1):
            if (rotten_after[row - 1][col] == 0 or rotten_after[row - 1][col] > rotten_after[row][col] + 1):
                rotten_after[row - 1][col] = rotten_after[row][col] + 1
                self.dfs(rotten_after, grid, row-1, col)
                
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get rows number
        rows = len(grid)
        if rows == 0:
            return -1
            
        # Get columns number
        cols = len(grid[0])

        # Define rotten_after
        rotten_after = [[0] * cols for _ in range(rows)]
        
        # Execute DFS for all rotten oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    self.dfs(rotten_after, grid, row, col)

        # Check if there are any fresh oranges left, if so return -1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and rotten_after[row][col] == 0:
                    return -1

        # Get the maximum time in the rotten_after array
        res = -1
        for row in range(rows):
            for col in range(cols):
                res = max(res, rotten_after[row][col])

        return res
