#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (58.68%)
# Likes:    659
# Dislikes: 22
# Total Accepted:    37.4K
# Total Submissions: 63.6K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
# 
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
# 
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
# 
# Given a puzzle board, return the least number of moves required so that the
# state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
# 
# Examples:
# 
# 
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# 
# 
# 
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# 
# 
# 
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# 
# 
# 
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# 
# 
# Note:
# 
# 
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
# 
# 
#

from typing import List
# @lc code=start

import copy
from collections import deque

class Node:
    def __init__(self, board, zero_loc, steps):
        self.board = board
        self.zero_loc = zero_loc
        self.steps = steps

class Solution:
    ''' BFS. use a queue. a state of a board is a node, the moves are edges and lead to a new node. use a dict to momorize the nodes visited.
        to improve time, don't use the direction array and operate all on one dimension string such as "123450"
        without direction array, use a dictionary that specify all the directions to go for each location. 
        moves = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }
    '''
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        zero_loc = None
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    zero_loc = (i, j)
        visited = set()
        queue = deque()
        queue.append(Node(board, zero_loc, 0))
        visited.add(tuple(board[0] + board[1]))
        final = [[1, 2, 3], [4, 5, 0]]
        while queue:
            node = queue.popleft()
            board = node.board
            zero_loc = node.zero_loc
            steps    = node.steps
            if board == final:
                return steps

            for d in directions:
                new_loc = (zero_loc[0] + d[0], zero_loc[1] + d[1])
                if 0 <= new_loc[0] <= 1 and 0 <= new_loc[1] <= 2:
                    new_board = copy.deepcopy(board)
                    new_board[new_loc[0]][new_loc[1]], new_board[zero_loc[0]][zero_loc[1]] = new_board[zero_loc[0]][zero_loc[1]], new_board[new_loc[0]][new_loc[1]]  # swap
                    if tuple(new_board[0] + new_board[1]) not in visited:
                        queue.append(Node(new_board, new_loc, steps + 1))
                        visited.add(tuple(new_board[0] + new_board[1]))
        return -1  # when the queue is empty and haven't reached the final board
# @lc code=end

'''
[[1,2,3],[4,0,5]]
[[1,2,3],[5,4,0]]
[[4,1,2],[5,0,3]]
[[3,2,4],[1,5,0]]
[[1,2,3],[4,5,0]]
'''