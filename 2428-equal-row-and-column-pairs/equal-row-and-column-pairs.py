class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}
        result = 0

        for i in range(len(grid)):
            if tuple(grid[i]) not in count:
                count[tuple(grid[i])] = 1
            elif tuple(grid[i]) in count:
                count[tuple(grid[i])] += 1

        for n in range(len(grid)):
            col = [i[n] for i in grid]
            if col in grid:
                result+=count[tuple(col)]
        return result
        