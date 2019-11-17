#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (40.62%)
# Likes:    1267
# Dislikes: 58
# Total Accepted:    166.9K
# Total Submissions: 394K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# Example:
# 
# 
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
# 
# 
#

from typing import List

# @lc code=start
class Solution:

    def __init__(self, chessboard=None, n=None):
        self.chessboard = chessboard
        self.n = n
        self.answers = []

    def check(self, row, col):
        '''check wether there is conflict for a new position (row, col)
        Args:
            chessboard -- list<int>
        '''
        for i in range(row):
            if col == self.chessboard[i]:                      # vertical
                return False
            if abs(row - i) == abs(col - self.chessboard[i]):  # diagonal
                return False
        return True

    @staticmethod
    def chessboard2list(chessboard, n):
        output = []
        for col in chessboard:
            tmp = ['.'] * n
            tmp[col] = 'Q'
            output.append(''.join(tmp))
        return output

    def backtrack(self, row):
        for col in range(self.n):
            if self.check(row, col):
                backup = self.chessboard[row]
                self.chessboard[row] = col
                if row == self.n - 1:
                    self.answers.append(Solution.chessboard2list(self.chessboard, self.n))
                else:
                    self.backtrack(row+1)
                    self.chessboard[row] = backup


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.answers = []
        self.n = n
        self.chessboard = [0] * n  # use 1d list to represent 2d chessboard
        self.backtrack(0)                        # start at zero-th row
        return self.answers


def test(n):
    s = Solution()
    answers = s.solveNQueens(n)
    for answer in answers:
        for row in answer:
            print(row)
        print()

if __name__ == '__main__':
    test(4)

# @lc code=end

