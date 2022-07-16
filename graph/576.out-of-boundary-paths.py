#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

from collections import Counter

# @lc code=start
class Solution:
    '''BFS + DP
       O(m*n*maxMove)
       Actually you don't need to do BFS, no queue required. Just iterate through the  n*m grid
       but a dp_temp and dp are needed. because if only dp, updating an element in dp will affect other elements
    '''
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dp = Counter()
        queue = [(0, startRow, startColumn)]   # (# of steps, current x, current y)
        dp[(0, startRow, startColumn)] += 1
        while queue:
            new_queue = []
            new_dp = Counter()
            for state in queue:
                step, cur_x, cur_y = state
                for dx, dy in directions:
                    nxt_x = cur_x + dx
                    nxt_y = cur_y + dy
                    if (nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n):  # out of bound
                        if step + 1 <= maxMove:
                            ans += dp[(step, cur_x, cur_y)]
                    else:                                                     # still in bound
                        if step + 1 < maxMove:
                            if new_dp[(step+1, nxt_x, nxt_y)] == 0:           # first time visit
                                new_queue.append((step+1, nxt_x, nxt_y))
                            new_dp[((step+1, nxt_x, nxt_y))] += dp[(step, cur_x, cur_y)]
            queue = new_queue
            dp = new_dp
        return ans % (10**9 + 7)

m = 3
n = 8
maxMove = 0
startRow = 2
startColumn = 0
s = Solution()
print(s.findPaths(m, n, maxMove, startRow, startColumn))

        
# @lc code=end

