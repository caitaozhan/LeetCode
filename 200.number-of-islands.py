#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.39%)
# Likes:    3580
# Dislikes: 131
# Total Accepted:    484.5K
# Total Submissions: 1.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

from typing import List

# @lc code=start
class Solution:

    def __init__(self):
        self.x_len = 0
        self.y_len = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.start_set = set()

    def init(self, grid):
        self.x_len = len(grid)
        try:
            self.y_len = len(grid[0])
        except:
            raise Exception()
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    self.start_set.add((i, j))

    def random_start(self):
        '''find a starting point for DFS
        '''
        if self.start_set:
            return self.start_set.pop()
        return None

    def check_boarder(self, point):
        x, y = point[0], point[1]
        if x < 0 or y < 0 or x >= self.x_len or y >= self.y_len:
            return False
        return True

    def bfs(self, start, grid):
        ''' do a bfs on grid starting at start
        '''
        queue = [start]
        while queue:
            cur = queue.pop(0)
            if grid[cur[0]][cur[1]] == '0':   # an element can be put in queue multiple times?
                continue
            if cur in self.start_set:
                self.start_set.remove(cur)

            grid[cur[0]][cur[1]] = '0'
            for d in self.directions:
                nxt = (cur[0] + d[0], cur[1] + d[1])
                if self.check_boarder(nxt) is False:
                    continue
                if grid[nxt[0]][nxt[1]] == '1':
                    queue.append(nxt)

    def numIslands(self, grid: List[List[str]]) -> int:
        try:
            self.init(grid)
        except:
            return 0
        counter = 0
        start = self.random_start()
        while start is not None:
            counter += 1
            # print('\n\n***\n', start, counter)
            self.bfs(start, grid)
            start = self.random_start()
        return counter


def test():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    s = Solution()
    print(s.numIslands(grid))
    
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    s = Solution()
    print(s.numIslands(grid))

def test2():
    grid = [["1"],["1"]]
    s = Solution()
    print(s.numIslands(grid))


if __name__ == '__main__':
    # test()
    # test2()
    pass
        
# @lc code=end

