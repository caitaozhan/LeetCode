#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
# https://leetcode.com/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (39.31%)
# Likes:    919
# Dislikes: 59
# Total Accepted:    66.3K
# Total Submissions: 168.5K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# A sequence of numbers is called a wiggle sequence if the differences between
# successive numbers strictly alternate between positive and negative. The
# first difference (if one exists) may be either positive or negative. A
# sequence with fewer than two elements is trivially a wiggle sequence.
# 
# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences
# (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5]
# and [1,7,4,5,5] are not wiggle sequences, the first because its first two
# differences are positive and the second because its last difference is zero.
# 
# Given a sequence of integers, return the length of the longest subsequence
# that is a wiggle sequence. A subsequence is obtained by deleting some number
# of elements (eventually, also zero) from the original sequence, leaving the
# remaining elements in their original order.
# 
# Example 1:
# 
# 
# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# 
# 
# Example 2:
# 
# 
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is
# [1,17,10,13,10,16,8].
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2
# 
# Follow up:
# Can you do it in O(n) time?
# 
# 
# 
#

from typing import List

# @lc code=start

class Solution2:
    ''' Keep recording the difference of the past two elements. 
        If multiple differences keep positive (or negative), keep the last one (the biggest or smallest)
    '''
    def difference(self, a, b):
        if b > a:
            return 1
        elif b < a:
            return -1
        else:  # a == b
            return 0

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        signs = []
        for i in range(1, len(nums)):
            sign = self.difference(nums[i-1], nums[i])
            if sign != 0:
                signs.append(sign)
    
        if len(signs) == 0:
            return 1

        counter = 1            # the fist one sign always count
        last = 0
        for i in range(1, len(signs)):
            if signs[i] != signs[last]:
                counter += 1
                last = i
        return counter + 1     # number of signs plus 1 equals to the number of numbers


class Solution3:
    '''Same greedy idea as Solution2, but a different implementation using a stack
    '''
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        sol = [nums[0]]  # the 0th element will always be in
        state = ''  # up or down
        for i in range(1, len(nums)):
            if nums[i] > sol[-1]:
                if state == 'up':
                    sol.pop(-1)
                else:
                    state = 'up'
                sol.append(nums[i])
            elif nums[i] < sol[-1]:
                if state == 'down':
                    sol.pop(-1)
                else:
                    state = 'down'
                sol.append(nums[i])
            else:  # ==
                pass
        return len(sol)


class Solution:
    '''a smart solution with very small memory usage
    '''
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        # positive is the max wiggle subsequence when the latest trend is positive, vise versa
        positive, negative = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                positive = negative + 1
            elif nums[i] < nums[i-1]:
                negative = positive + 1
        return max(positive, negative)

# @lc code=end

'''

[0,0]

'''