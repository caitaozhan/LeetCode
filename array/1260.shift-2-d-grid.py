#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def shift(grid):
            new_grid = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        new_grid[0][0] = grid[i][j]
                    elif j == n - 1:
                        new_grid[i + 1][0] = grid[i][j]
                    else:
                        new_grid[i][j + 1] = grid[i][j]
            return new_grid

        for _ in range(k):
            grid = shift(grid)
        
        return grid



class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        new_grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_j = j + k
                i_increase = new_j // n
                new_i = i + i_increase
                new_i = new_i % m
                new_j = new_j % n
                new_grid[new_i][new_j] = grid[i][j]
        
        return new_grid

# @lc code=end

