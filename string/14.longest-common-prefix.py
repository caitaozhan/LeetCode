#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.16%)
# Likes:    2656
# Dislikes: 1889
# Total Accepted:    771.1K
# Total Submissions: 2.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if len(strs) == 0 or len(strs[0]) == 0:
            return prefix
        
        size = len(strs[0])
        i = 0
        terminate = False
        while i < size and not terminate:
            ch = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != ch:
                    terminate = True
                    break
            else:
                prefix += ch
            i += 1
        return prefix
# @lc code=end

