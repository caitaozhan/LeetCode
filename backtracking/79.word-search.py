#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

from typing import List

# @lc code=start
class Solution:
    '''DFS, version 1
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, idx: int, visited: list) -> bool:
            if idx == len(word) - 1:
                return board[x][y] == word[idx]
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nxt_x = x + d[0]
                nxt_y = y + d[1]
                if 0 <= nxt_x < self.m and 0 <= nxt_y < self.n and visited[nxt_x][nxt_y] == 0:
                    if board[nxt_x][nxt_y] == word[idx + 1]:
                        visited[nxt_x][nxt_y] = 1
                        ret = dfs(nxt_x, nxt_y, idx + 1, visited)
                        visited[nxt_x][nxt_y] = 0
                        if ret:
                            return True
            return False

        self.m = len(board)
        self.n = len(board[0])
        # find the starting locations and do a DFS
        start = word[0]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == start:
                    visited = [[0] * self.n for _ in range(self.m)]
                    visited[i][j] = 1
                    if dfs(i, j, idx=0, visited=visited):
                        return True
        return False


class Solution:
    '''DFS, version 2, slightly difference place to put visited array
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, idx: int, visited: list) -> bool:
            if idx == len(word) - 1:
                return board[x][y] == word[idx]
            visited[x][y] = 1
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nxt_x = x + d[0]
                nxt_y = y + d[1]
                if 0 <= nxt_x < self.m and 0 <= nxt_y < self.n and visited[nxt_x][nxt_y] == 0:
                    if board[nxt_x][nxt_y] == word[idx + 1]:
                        if dfs(nxt_x, nxt_y, idx + 1, visited):
                            return True
            visited[x][y] = 0
            return False

        self.m = len(board)
        self.n = len(board[0])
        # find the starting locations and do a DFS
        start = word[0]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == start:
                    visited = [[0] * self.n for _ in range(self.m)]
                    if dfs(i, j, idx=0, visited=visited):
                        return True
        return False



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word = "AAAAAAAAAAAAABB"

s = Solution()
print(s.exist(board, word))
        
# @lc code=end

