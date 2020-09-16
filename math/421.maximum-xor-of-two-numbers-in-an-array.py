#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (53.20%)
# Likes:    1438
# Dislikes: 180
# Total Accepted:    59.6K
# Total Submissions: 111.8K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 2^31.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# 
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        size = len(bin(max(nums))) - 2
        max_xor = 0
        for i in reversed(range(size)):
            max_xor <<= 1
            cur_xor = max_xor | 1
            prefixes = {num>>i for num in nums}
            for prefix in prefixes:
                if prefix ^ cur_xor in prefixes:
                    max_xor |= 1
                    break
        return max_xor


def test():
    nums = [3, 10, 5, 25, 2, 8]
    s = Solution()
    print(s.findMaximumXOR(nums))

test()

# @lc code=end

