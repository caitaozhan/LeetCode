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
        self.route = []                                 # define a backtrack route (fill the subbox first)
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





class SolutionOther:  # fastest solution on LeetCode
# Idea:
    # Keep track of 
    # 1. all empty spots along with all candidate digits that can be placed at those spots
    # - Use DFS to try the empty spot with fewest candidates (using 1) (optimization)
    # - Try place each candidate at that spot.
    # - Scan through all other empty spots and modify their candidate ditis
    #   if they are affected by this placement. (keep track of this update)
    #   Terminate early if any other spot loses all candidates. (important optimization)
    # - Backtrack if this path failed, and un-modify all the changes made.
    def solveSudoku(self, board):
        """
        [List [List String]] -> Void
        Solve the given board of 9x9 sudoku, modify the board in place.
        """

        # [Map (Int, Int) [Set Int]]
        # Keys are remaining empty spots during the search represented as (row, col).
        # Values are the candidate digits that can be placed at (row, col)
        empty_spots = {}

        # row_valids[i] is a Set of digits which is found at i-th row in board
        row_digits = [set() for j in range(9)]
        # col_valids[i] is a Set of digits which is found at i-th column in board
        col_digits = [set() for j in range(9)]
        # sqr_valids[i] is a Set of digits which is found at i-th square in board
        sqr_digits = [set() for j in range(9)]

        # convert strings in the board to integers
        # fill in the above lists during this process
        int_board = []
        for row in range(9):
            int_row = []
            for col in range(9):
                s = board[row][col]
                sqr = (row // 3) * 3 + (col // 3)
                if s.isdigit():
                    num = int(s)
                    int_row.append(num)
                    row_digits[row].add(num)
                    col_digits[col].add(num)
                    sqr_digits[sqr].add(num)
                else:
                    int_row.append(0)
                    empty_spots[(row, col)] = set()
            int_board.append(int_row)

        # fill in empty_spots
        for row, col in empty_spots:
            candidates = empty_spots[(row, col)]
            sqr = (row // 3) * 3 + (col // 3)
            for n in range(1, 10):
                # if n is can be placed at (row, col) and sqr-th square
                # it's a valid candidate for (row, col)
                if not (n in row_digits[row] or n in col_digits[col] or n in sqr_digits[sqr]):
                    candidates.add(n)


        def dfs():
            # Try filling in each empty spot per rule of sudoku,
            # do a dfs and backtrack to look for a potential solution.
            # Modify the board in place and return True iff a solution was found.

            # if no more empty spots left, a solution was found
            if not empty_spots:
                return True

            # find the empty spot with fewest candidates
            target_row, target_col = min([spot for spot in empty_spots], key=lambda s : len(empty_spots[s]))
            target_sqr = (target_row // 3) * 3 + (target_col // 3)
            candidates = empty_spots[(target_row, target_col)]

            # remove this from empty_spots
            del empty_spots[(target_row, target_col)]
            # try placing each candidate at (target_row, target_col)
            for n in candidates:
                # for rest of empty spots, if they are in the same row/col/sqr
                # as n, and contains n, they need to be updated. We keep
                # track of these updates in case of backtracking
                updated_spots = []
                # whether the placement of n failed (invalidates other empty spots)
                failed = False
                for spot, valids in empty_spots.items():
                    row, col = spot
                    sqr = (row // 3) * 3 + (col // 3)
                    if n in valids and (target_row == row or target_col == col or target_sqr == sqr):
                        valids.remove(n)
                        updated_spots.append(spot)
                    if not valids:
                        failed = True
                        break

                # If the placement was successful,
                # keep doing the dfs with leftover empty spots
                if not failed and dfs():
                    # modify the board iff a solution was found
                    # this keeps number of modification minimal
                    int_board[target_row][target_col] = n
                    return True

                # Backtrack and un-modify all changes
                for spot in updated_spots:
                    empty_spots[spot].add(n)
                int_board[target_row][target_col] = 0
                

            # All candidates failed, this path of search should be abandonded.
            # Restore the target to empty_spots and backtrack
            empty_spots[(target_row, target_col)] = candidates
            return False

        if not dfs():
            raise RuntimeError("No solution possible for given board")
        
        # Write solution back into the original board
        for row in range(9):
            for col in range(9):
                board[row][col] = str(int_board[row][col])

