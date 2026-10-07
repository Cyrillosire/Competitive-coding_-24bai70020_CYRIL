from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if visited[r][c] or grid[r][c] == '0':
                return

            visited[r][c] = True

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    count += 1

        return count


m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

grid = []

print("Enter the grid:")
for i in range(m):
    row = input(f"Row {i + 1}: ").split()
    grid.append(row)

solution = Solution()
result = solution.numIslands(grid)

print("Number of islands:", result)