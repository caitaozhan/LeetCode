''' 
You are starving and you want to eat food as quickly as possible. 
You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location 
if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. 
If there is no path for you to reach food, return -1.
'''

from typing import List

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start = None
        for i in range(m):
            for j in range(n):
                if start is not None:
                    break
                if grid[i][j] == '*':
                    start = (i, j)
            
        visited = [[0] * n for _ in range(m)]
        queue = [start]
        visited[start[0]][start[1]] = 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        steps = 0
        while queue:
            new_queue = []
            for node in queue:
                for dx, dy in directions:
                    nxt_x = node[0] + dx
                    nxt_y = node[1] + dy
                    if 0 <= nxt_x < m and 0 <= nxt_y < n:
                        if grid[nxt_x][nxt_y] == 'X' or visited[nxt_x][nxt_y] == 1:
                            continue
                        if grid[nxt_x][nxt_y] == '#':
                            return steps + 1
                        new_queue.append((nxt_x, nxt_y))
                        visited[nxt_x][nxt_y] = 1
            queue = new_queue
            steps += 1
        return -1

