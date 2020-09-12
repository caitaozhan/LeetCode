#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (55.78%)
# Likes:    1244
# Dislikes: 54
# Total Accepted:    180.6K
# Total Submissions: 313.9K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start

import itertools
from typing import List

class SolutionIter:
    '''time beat 95%
    '''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [nums for nums in itertools.combinations(range(1, 10), k) if sum(nums) == n]


class Solution:
    '''backtracking
    '''
    def __init__(self):
        self.ans = []
        self.k = 0
        self.n = 0

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k, self.n = k, n
        self.backtrack(1, [])
        return self.ans
    
    def backtrack(self, idx, lst):
        if len(lst) == self.k:
            if sum(lst) == self.n:
                self.ans.append(lst[:])
            return
        if sum(lst) > self.n:
            return

        for i in range(idx, 10):
            lst.append(i)
            self.backtrack(i+1, lst)
            lst.pop()

s = Solution()
print(s.combinationSum3(3, 9))

# @lc code=end

