#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
# https://leetcode.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (59.86%)
# Likes:    363
# Dislikes: 17
# Total Accepted:    18.1K
# Total Submissions: 30.1K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island
# totally (all left, top, right, bottom) surrounded by 1s.
# 
# Return the number of closed islands.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).
# 
# Example 2:
# 
# 
# 
# 
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠              [1,1,1,1,1,1,1]]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
#

from typing import List
from collections import deque

# @lc code=start
class Solution2:
    '''bfs
    '''
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.m = 0
        self.n = 0
    
    def at_edge(self, i, j):
        if i == 0 or j == 0 or i == self.m-1 or j == self.n-1:
            return True
        return False

    def check_boarder(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n:
            return True
        return False

    def bfs(self, i, j, grid):
        '''Do a bfs starting at (i, j)
        '''
        closed = True
        queue = deque([(i, j)])
        grid[i][j] = 1
        while queue:
            x, y = queue.popleft()
            if closed and self.at_edge(x, y):
                closed = False
            for d in self.directions:
                nxt_x = x + d[0]
                nxt_y = y + d[1]
                if self.check_boarder(nxt_x, nxt_y) and grid[nxt_x][nxt_y] == 0:
                    queue.append((nxt_x, nxt_y))
                    grid[nxt_x][nxt_y] = 1
                    if closed and self.at_edge(nxt_x, nxt_y):
                        closed = False
        return closed

    def closedIsland(self, grid: List[List[int]]) -> int:
        counter = 0
        m, n = len(grid), len(grid[0])
        self.m, self.n = m, n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closed = self.bfs(i, j, grid)
                    if closed:
                        counter += 1
        return counter


class Solution:

    def dfs(self, i, j, grid, closed):
        '''
        '''
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            closed[0] = False
        elif grid[i][j] == 0:
            grid[i][j] = 2
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for d in directions:
                nxt_x = i + d[0]
                nxt_y = j + d[1]
                self.dfs(nxt_x, nxt_y, grid, closed)

    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closed = [True]
                    self.dfs(i, j, grid, closed)
                    if closed[0]:
                        counter += 1
        return counter

# @lc code=end

