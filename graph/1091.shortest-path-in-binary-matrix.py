#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

from collections import defaultdict

# @lc code=start
class Solution:
    '''BFS, no need to build graph as the first step
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        length = 1
        visited = [[0 for _ in range(n)] for _ in range(n)]
        end = (n - 1, n - 1)
        queue = [(0, 0)]
        visited[0][0] = 1
        while queue:
            new_queue = []
            for node in queue:
                if node == end:
                    return length
                for d in directions:
                    x = node[0] + d[0]
                    y = node[1] + d[1]
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and visited[x][y] == 0:
                        new_queue.append((x, y))
                        visited[x][y] = 1
            queue = new_queue
            length += 1
        
        return -1




# @lc code=end

