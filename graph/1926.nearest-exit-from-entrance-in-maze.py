#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

from typing import List

# @lc code=start
class Solution:

    def in_bound(self, loc, m, n):
        if 0 <= loc[0] < m and 0 <= loc[1] < n:
            return True
        return False

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        steps = 0
        queue = [entrance]
        visited[entrance[0]][entrance[1]] = 1  # bug: forgot this line ...
        while queue:
            new_queue = []
            for cur in queue:
                for d in directions:
                    nxt = [cur[0] + d[0], cur[1] + d[1]]
                    if self.in_bound(nxt, m, n):
                        if maze[nxt[0]][nxt[1]] == '+' or visited[nxt[0]][nxt[1]] == 1: # hit wall or already visited
                            continue
                        else:                              # good cell
                            new_queue.append(nxt)
                            visited[nxt[0]][nxt[1]] = 1    # mark visited after putting nxt into the queue
                    else:
                        if steps > 0:
                            return steps                   # return the ans
                        else:
                            pass                           # entrance doesn't count
            queue = new_queue
            steps += 1
        return -1


maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
maze = [[".","."]]
entrance = [0,1]
s = Solution()
print(s.nearestExit(maze, entrance))


# @lc code=end

