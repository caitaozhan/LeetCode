#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        grid = [[0 for _ in range(n)] for _ in range(n)]
        total = n**2
        counter = 0
        cur = [0, -1]
        stop = False
        while stop is False:
            steps = [n, n-1, n-1, n-2]
            for d, step in zip(directions, steps):
                for _ in range(step):
                    cur = [cur[0] + d[0], cur[1] + d[1]]
                    counter += 1
                    grid[cur[0]][cur[1]] = counter
                if counter == total:
                    stop = True
                    break
            n -= 2
        return grid


        
# @lc code=end

