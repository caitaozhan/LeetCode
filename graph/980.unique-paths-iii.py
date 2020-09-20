#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20

"""

from typing import List

# @lc code=start
class Solution:
    '''backtracking in a graph, time complexity is O(3^n)
    '''
    def __init__(self):
        self.ans = 0
        self.grid = []
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.start = 0
        self.end = 0
        self.non_obstacle = 0
        self.x_len = 0
        self.y_len = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.x_len, self.y_len = len(grid), len(grid[0])
        self.grid = grid
        for i in range(self.x_len):
            for j in range(self.y_len):
                if grid[i][j] == 0:
                    self.non_obstacle += 1
                elif grid[i][j] == 1:
                    self.start = (i, j)
                elif grid[i][j] == 2:
                    self.end = (i, j)
                else:
                    pass
        visited = [[False for _ in range(self.y_len)] for _ in range(self.x_len)]
        self.backtrack(self.start, 0, visited)
        return self.ans

    def backtrack(self, cur, path_len, visited):
        visited[cur[0]][cur[1]] = True
        for i, j in self.directions:
            nxt = (cur[0]+i, cur[1]+j)
            if 0 <= nxt[0] < self.x_len and 0 <= nxt[1] < self.y_len and visited[nxt[0]][nxt[1]] == False:
                if self.grid[nxt[0]][nxt[1]] == 0:
                    self.backtrack(nxt, path_len+1, visited)
                elif self.grid[nxt[0]][nxt[1]] == -1:
                    continue
                elif self.grid[nxt[0]][nxt[1]] == 2:
                    if path_len == self.non_obstacle:
                        self.ans += 1
                    else:
                        continue
        visited[cur[0]][cur[1]] = False
        
# @lc code=end

