#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        prefix_sum = [[0 for _ in range(n)] for _ in range(m)]
        
        def helper(i, j):
            if i <= -1 or i >= m or j <= -1:
                return 0
            elif j >= n:
                return prefix_sum[i][n-1]
            else:
                return prefix_sum[i][j]

        for i in range(m):
            for j in range(n):
                prefix_sum[i][j] = helper(i, j-1) + board[i][j]
        
        for i in range(m):
            for j in range(n):
                summ  = helper(i-1, j+1) - helper(i-1, j-2)
                summ += helper(i,   j+1) - helper(i,   j-2)
                summ -= board[i][j]
                summ += helper(i+1, j+1) - helper(i+1, j-2)
                if board[i][j] == 0: # reproduce
                    if summ == 3:
                        board[i][j] = 1
                else:
                    if summ < 2 or summ > 3:     # die
                        board[i][j] = 0
                    

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        The key is to introduce two new states other than 0 and 1
        -1 means originally is 1, died, turns into 0
        2  means originally is 0, become alive, turns into 1
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                row1 = max(0, i-1)
                row2 = min(m, i+2)
                col1 = max(0, j-1)
                col2 = min(n, j+2)
                summ = 0
                for x in range(row1, row2):
                    for y in range(col1, col2):
                        if x == i and y == j:
                            continue
                        if board[x][y] == 1 or board[x][y] == -1:
                            summ += 1
                if board[i][j] == 0:
                    if summ == 3:
                        board[i][j] = 2    # reproduce
                else:
                    if summ < 2 or summ > 3:
                        board[i][j] = -1   # die

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
                else:
                    pass
        


# @lc code=end

