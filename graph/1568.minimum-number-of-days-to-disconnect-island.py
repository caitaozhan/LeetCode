"""

Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:



Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
Example 3:

Input: grid = [[1,0,1,0]]
Output: 0
Example 4:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1
Example 5:

Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is 0 or 1

"""



from typing import List

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def check_bound(self, cur, grid):
        x_len, y_len = len(grid), len(grid[0])
        if 0 <= cur[0] < x_len and 0 <= cur[1] < y_len:
            return True
        return False

    def count_islands(self, grid):
        counter = 0
        x_len, y_len = len(grid), len(grid[0])
        visited = [[0]*y_len for _ in range(x_len)]
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    counter += 1
                    self.dfs((i, j), grid, visited)
        return counter

    def dfs(self, cur, grid, visited):
        visited[cur[0]][cur[1]] = 1
        for d in self.directions:
            nxt = (cur[0] + d[0], cur[1] + d[1])
            if self.check_bound(nxt, grid) and grid[nxt[0]][nxt[1]] == 1 and visited[nxt[0]][nxt[1]] == 0:
                self.dfs(nxt, grid, visited)

    def minDays(self, grid: List[List[int]]) -> int: 
        if self.count_islands(grid) >= 2:
            return 0
        x_len = len(grid)
        y_len = len(grid[0])
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.count_islands(grid) >= 2:
                        return 1
                    grid[i][j] = 1
        return 2
