#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (49.82%)
# Likes:    805
# Dislikes: 171
# Total Accepted:    84.7K
# Total Submissions: 169.4K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
# the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
# 
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# 
# Return the minimum number of rotations so that all the values in A are the
# same, or all the values in B are the same.
# 
# If it cannot be done, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do
# any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
# 
# 
# Example 2:
# 
# 
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # either all A[0] or all B[0]. so these two are the candidates
        candidateA = [A[0], True, 0, 0]  # number of A[0] in A and B respectively
        candidateB = [B[0], True, 0, 0]  # number of B[0] in A and B respectively
        for i in range(len(A)):
            if A[i] == candidateA[0]:
                candidateA[2] += 1
            if B[i] == candidateA[0]:
                candidateA[3] += 1
            if candidateA[0] not in [A[i], B[i]]:
                candidateA[1] = False
            
            if A[i] == candidateB[0]:
                candidateB[2] += 1
            if B[i] == candidateB[0]:
                candidateB[3] += 1
            if candidateB[0] not in [A[i], B[i]]:
                candidateB[1] = False
            
            if candidateA[1] is False and candidateB[1] is False:
                return -1
        
        ans = float('inf')
        if candidateA[1] is True:
            ans = min(ans, len(A) - candidateA[2], len(A) - candidateA[3])
        if candidateB[1] is True:
            ans = min(ans, len(A) - candidateB[2], len(A) - candidateB[3])
        return ans
# @lc code=end

