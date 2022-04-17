#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

from collections import Counter

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            counter = Counter()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if counter[board[i][j]] == 1:
                    return False
                counter[board[i][j]] = 1
        
        # check column
        for j in range(9):
            counter = Counter()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if counter[board[i][j]] == 1:
                    return False
                counter[board[i][j]] = 1
        
        # check subbox
        for box_i in range(3):
            for box_j in range(3):
                counter = Counter()
                start_i = 3 * box_i
                start_j = 3 * box_j
                for i in range(3):
                    for j in range(3):
                        x = start_i + i
                        y = start_j + j
                        if board[x][y] == '.':
                            continue
                        if counter[board[x][y]] == 1:
                            return False
                        counter[board[x][y]] = 1

        return True

        
# @lc code=end

