#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

from typing import List

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = {}
        state = (0, 0, k)    # (location_i, location_j, elimination left)
        queue = [state]
        visited[(0, 0)] = k
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        steps = 0
        while queue:
            new_queue = []
            for x, y, e in queue:
                if x == m - 1 and y == n - 1:
                    return steps
                for dx, dy in directions:
                    nxt_x = x + dx
                    nxt_y = y + dy
                    if 0 <= nxt_x < m and 0 <= nxt_y < n:
                        if grid[nxt_x][nxt_y] == 0:  # no obstacle
                            if (nxt_x, nxt_y) not in visited:
                                new_queue.append((nxt_x, nxt_y, e))
                                visited[(nxt_x, nxt_y)] = e
                            else:
                                if visited[(nxt_x, nxt_y)] < e: # visited before, but previous visit has a smaller k, so current visit still valuable
                                    new_queue.append((nxt_x, nxt_y, e))
                                    visited[(nxt_x, nxt_y)] = e
                        else:  # obstacle
                            if e == 0:
                                continue
                            if (nxt_x, nxt_y) not in visited:
                                new_queue.append((nxt_x, nxt_y, e - 1))
                                visited[(nxt_x, nxt_y)] = e - 1
                            else:
                                if visited[(nxt_x, nxt_y)] < e - 1:
                                    new_queue.append((nxt_x, nxt_y, e - 1))
                                    visited[(nxt_x, nxt_y)] = e - 1
            queue = new_queue
            steps += 1
        return -1

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
s = Solution()
print(s.shortestPath(grid, k))
        
# @lc code=end

