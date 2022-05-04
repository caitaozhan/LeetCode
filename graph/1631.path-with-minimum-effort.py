#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

from collections import deque
from typing import List

# @lc code=start
class Solution:
    '''bfs
    '''
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        queue = deque()
        queue.append((0, 0, 0))  # (x, y, min_effort)
        dp[0][0] = 0
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            cur_x, cur_y, effort = queue.popleft()
            if effort > dp[cur_x][cur_y]:  # key pruning trick
                continue
            for d in direction:
                nxt_x = cur_x + d[0]
                nxt_y = cur_y + d[1]
                if 0 <= nxt_x < n and 0 <= nxt_y < m:
                    new_effort = max(effort, abs(heights[nxt_x][nxt_y] - heights[cur_x][cur_y]))
                    if new_effort < dp[nxt_x][nxt_y]:
                        dp[nxt_x][nxt_y] = new_effort
                        queue.append((nxt_x, nxt_y, new_effort))
        return dp[-1][-1]





# @lc code=end

