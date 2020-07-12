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
class Solution3:
    '''this solution is correct, but pretty slow because of bad position of changing grid[][]
    '''
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
            self.bfs(start, grid)
            start = self.random_start()
        return counter


class Solution2:
    def __init__(self):
        self.x_len = 0
        self.y_len = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def check(self, x, y):
        '''check whether (x, y) is inside the grid'''
        if x < 0 or y < 0 or x >= self.x_len or y >= self.y_len:
            return False
        return True

    def bfs(self, x, y, grid):
        '''do a bfs starting at (x, y) in grid
        '''
        grid[x][y] = '0'                         # mark as visited
        queue = [(x, y)]
        while queue:
            cur = queue.pop(0)
            for d in self.directions:
                nxt_x = cur[0] + d[0]
                nxt_y = cur[1] + d[1]
                if self.check(nxt_x, nxt_y) is True and grid[nxt_x][nxt_y] == '1':
                    grid[nxt_x][nxt_y] = '0'   # mark as visited
                    queue.append((nxt_x, nxt_y))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.x_len = len(grid)
        try:
            self.y_len = len(grid[0])
        except:
            return 0

        counter = 0
        for x in range(self.x_len):
            for y in range(self.y_len):
                if grid[x][y] == '1':
                    counter += 1
                    self.bfs(x, y, grid)
        return counter


class Solution4:
    '''dfs
    '''
    def __init__(self):
        self.x_len = 0
        self.y_len = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def check(self, x, y):
        '''check whether (x, y) is inside the grid'''
        if x < 0 or y < 0 or x >= self.x_len or y >= self.y_len:
            return False
        return True

    def dfs(self, x, y, grid):
        grid[x][y] = '0'
        for d in self.directions:
            nxt_x = x + d[0]
            nxt_y = y + d[1]
            if self.check(nxt_x, nxt_y) is True and grid[nxt_x][nxt_y] == '1':
                self.dfs(nxt_x, nxt_y, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.x_len = len(grid)
        try:
            self.y_len = len(grid[0])
        except:
            return 0

        counter = 0
        for x in range(self.x_len):
            for y in range(self.y_len):
                if grid[x][y] == '1':
                    counter += 1
                    self.dfs(x, y, grid)
        return counter

class UF:
    def __init__(self, m, n, grid):
        ''' m row n colomn grid
        '''
        self.counter = 0
        self.parent = [[0 for j in range(n)] for i in range(m)]  # the parent is itself
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.counter += 1
                    self.parent[i][j] = (i, j)

    def find(self, x, y):
        '''find the root and do path compression in the mean time
        '''
        while self.parent[x][y] != (x, y):
            parent_x, parent_y = self.parent[x][y]
            self.parent[x][y] = self.parent[parent_x][parent_y]  # path compression
            x, y = self.parent[x][y]
        return x, y
    
    def union(self, x, y, i, j):
        '''union (x, y) and (i, j)
        '''
        root_xy = self.find(x, y)
        root_ij = self.find(i, j)
        if root_xy != root_ij:
            self.parent[root_xy[0]][root_xy[1]] = root_ij
            self.counter -= 1


class Solution:
    '''union find solution
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        uf = UF(m, n, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    nxt_x = i + d[0]
                    nxt_y = j + d[1]
                    if 0 <= nxt_x < m and 0 <= nxt_y < n and grid[nxt_x][nxt_y] == '1':
                        uf.union(i, j, nxt_x, nxt_y)
        return uf.counter



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

def test3():
    grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    s = Solution()
    print(s.numIslands(grid))

if __name__ == '__main__':
    test()
    # test2()
    # test3()
    pass
        
# @lc code=end

