from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] != '1':
                return

            grid[r][c] = '0'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []

for i in range(m):
    row = input(f"Enter row {i + 1}: ").split()
    grid.append(row)

solution = Solution()
print("Number of islands:", solution.numIslands(grid))