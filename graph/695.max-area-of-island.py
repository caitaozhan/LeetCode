#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    '''dfs without a return, use a global variable instead to do the counting
    '''
    def __init__(self):
        self.counter = 0
        self.ans = 0
        self.m = 0
        self.n = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i: int, j: int):
            '''current node is (i, j)
            '''
            grid[i][j] = 0
            self.counter += 1
            for x, y in directions:
                nxt_i = i + x
                nxt_j = j + y
                if 0 <= nxt_i < self.m and 0 <= nxt_j < self.n and grid[nxt_i][nxt_j] == 1:
                    dfs(nxt_i, nxt_j)

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    continue
                self.counter = 0
                dfs(i, j)
                self.ans = max(self.ans, self.counter)
        return self.ans


class Solution:
    '''dfs with a return
    '''
    def __init__(self):
        self.counter = 0
        self.ans = 0
        self.m = 0
        self.n = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i: int, j: int) -> int:
            '''current node is (i, j), return the area starting from current node (inclusive)
            '''
            if 0 <= i < self.m and 0 <= j < self.n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1)
            else:
                return 0

        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    continue
                self.ans = max(self.ans, dfs(i, j))
        return self.ans

# @lc code=end

