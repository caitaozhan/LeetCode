#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#
# https://leetcode.com/problems/robot-bounded-in-circle/description/
#
# algorithms
# Medium (48.40%)
# Likes:    401
# Dislikes: 149
# Total Accepted:    24.9K
# Total Submissions: 47.6K
# Testcase Example:  '"GGLLGG"'
#
# On an infinite plane, a robot initially stands at (0, 0) and faces north.
# The robot can receive one of three instructions:
# 
# 
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# 
# 
# The robot performs the instructions given in order, and repeats them
# forever.
# 
# Return true if and only if there exists a circle in the plane such that the
# robot never leaves the circle.
# 
# 
# 
# Example 1:
# 
# 
# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to
# (0,0).
# When repeating these instructions, the robot remains in the circle of radius
# 2 centered at the origin.
# 
# 
# Example 2:
# 
# 
# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.
# 
# 
# Example 3:
# 
# 
# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) ->
# ...
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
# 
# 
#

# @lc code=start
from math import sqrt

class Solution2:
    ''' must come back to the origin in 4 cycles
    '''
    def isRobotBounded(self, instructions: str) -> bool:
        start_pos = [0, 0]
        start_dir = 0   # L -> -1    R -> +1
        direct = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cur_pos = [0, 0]
        cur_dir = 0
        for _ in range(4):
            for ch in instructions:
                if ch == 'G':
                    cur_pos = [cur_pos[0] + direct[cur_dir][0], cur_pos[1] + direct[cur_dir][1]]
                elif ch == 'L':
                    cur_dir = (cur_dir - 1) % 4
                elif ch == 'R':
                    cur_dir = (cur_dir + 1) % 4
            if cur_pos == start_pos and cur_dir == start_dir:
                return True
        return False

class Solution:
    ''' just run one cycle
    '''
    def isRobotBounded(self, instructions: str) -> bool:
        start_pos = [0, 0]
        start_dir = 0   # L -> -1    R -> +1
        direct = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cur_pos = [0, 0]
        cur_dir = 0
        for ch in instructions:
            if ch == 'G':
                cur_pos = [cur_pos[0] + direct[cur_dir][0], cur_pos[1] + direct[cur_dir][1]]
            elif ch == 'L':
                cur_dir = (cur_dir - 1) % 4
            elif ch == 'R':
                cur_dir = (cur_dir + 1) % 4
        if cur_pos == start_pos or cur_dir != start_dir:
            return True
        return False

# @lc code=end

