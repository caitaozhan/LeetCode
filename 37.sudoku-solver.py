#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (38.15%)
# Likes:    1200
# Dislikes: 76
# Total Accepted:    152.1K
# Total Submissions: 384.3K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#

from typing import List

# @lc code=start
class Solution:

    def __init__(self):
        self.box_len  = 3
        self.grid_len = 9
        self.subbox   = [ [ [0]*10 for _ in range(self.box_len)] for _ in range(self.box_len)] # counter for subbox. size is 10: trade memory for readability and time
        self.row      = [ [0]*10 for _ in range(self.grid_len)]                                # counter for each row
        self.column   = [ [0]*10 for _ in range(self.grid_len)]                                # counter for each column
        self.route    = []
        self.board    = [[]]
        self.flag     = False

    def init(self, board):
        '''init subbox, row, column'''
        self.board = board
        for i in range(self.grid_len):
            for j in range(self.grid_len):
                try:
                    number = int(board[i][j])         # raise exception when "."
                    self.row[i][number]    = 1        # number is the index
                    self.column[j][number] = 1
                    out_i = i // self.box_len
                    out_j = j // self.box_len
                    self.subbox[out_i][out_j][number] = 1
                except:
                    pass

    def check(self, number, loc):
        '''check whether number is valid at loc'''
        i, j  = loc[0], loc[1]
        out_i = i // self.box_len
        out_j = j // self.box_len
        if self.subbox[out_i][out_j][number] == 1:  # step 1: check subbox
            return False
        if self.row[i][number] == 1:                # step 2: check row
            return False
        if self.column[j][number] == 1:             # step 3: check column
            return False
        return True

    def put(self, number, loc):
        '''put the number at loc'''
        i, j  = loc[0], loc[1]
        out_i = i // self.box_len
        out_j = j // self.box_len
        self.board[i][j] = str(number)
        self.subbox[out_i][out_j][number] = 1
        self.row[i][number] = 1
        self.column[j][number] = 1

    def unput(self, number, loc):
        '''remove the number at loc'''
        i, j = loc[0], loc[1]
        out_i = i // self.box_len
        out_j = j // self.box_len
        self.subbox[out_i][out_j][number] = 0
        self.row[i][number] = 0
        self.column[j][number] = 0        

    def backtrack(self, indx):
        if indx == len(self.route):
            self.flag = True                   # found the single unique solution!
            return
        loc = self.route[indx]
        for number in range(1, 10):
            if self.flag is True:
                return
            if self.check(number, loc) is True:
                self.put(number, loc)
                self.backtrack(indx + 1)
                self.unput(number, loc)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.init(board)
        self.route = []                                 # define a backtrack route
        for out_i in range(self.box_len):               # index for the subbox
            for out_j in range(self.box_len):
                for in_i in range(self.box_len):        # index inside the subbox
                    for in_j in range(self.box_len):
                        i = out_i*self.box_len + in_i
                        j = out_j*self.box_len + in_j
                        if board[i][j] != '.':
                            continue
                        self.route.append((i, j))
        self.backtrack(0)                               # start at the zero-th index of the route


def test():
    board = \
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
    
    s = Solution()
    s.solveSudoku(board)
    for row in s.board:
        print(row)


if __name__ == '__main__':
    test()
        
# @lc code=end

