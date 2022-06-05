#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (53.07%)
# Likes:    349
# Dislikes: 129
# Total Accepted:    113.6K
# Total Submissions: 208.6K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#


# @lc code=start
class Solution:

    def __init__(self, chessboard=None, n=None):
        self.chessboard = chessboard
        self.n = n
        self.answers = 0

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

    def backtrack(self, row):
        for col in range(self.n):
            if self.check(row, col):
                self.chessboard[row] = col
                if row == self.n - 1:
                    self.answers += 1
                else:
                    self.backtrack(row+1)

    def totalNQueens(self, n: int) -> int:
        self.answers = 0
        self.n = n
        self.chessboard = [0] * n  # use 1d list to represent 2d chessboard
        self.backtrack(0)          # start at zero-th row
        return self.answers


class Solution:
    '''doing it again on 6/5/2022
    '''
    def __init__(self):
        self.ans = 0
        
    def totalNQueens(self, n: int) -> int:
        
        def check(row, col):
            for i in range(row):
                if col == board[i]:
                    return False
                if abs(board[i] - col) == abs(i - row):
                    return False
            return True
        
        def backtrack(row):
            if row == n:
                self.ans += 1
            for col in range(n):
                if check(row, col):
                    board[row] = col
                    backtrack(row + 1)
        
        board = [-1] * n
        backtrack(row = 0)
        return self.ans
        


def test(n):
    s = Solution()
    answers = s.totalNQueens(n)
    print(answers)


if __name__ == '__main__':
    test(4)
    test(8)       
# @lc code=end

