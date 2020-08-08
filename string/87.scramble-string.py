#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (33.32%)
# Likes:    530
# Dislikes: 722
# Total Accepted:    111K
# Total Submissions: 329.4K
# Testcase Example:  '"great"\n"rgeat"'
#
# Given a string s1, we may represent it as a binary tree by partitioning it to
# two non-empty substrings recursively.
# 
# Below is one possible representation of s1 = "great":
# 
# 
# ⁠   great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
# 
# 
# To scramble the string, we may choose any non-leaf node and swap its two
# children.
# 
# For example, if we choose the node "gr" and swap its two children, it
# produces a scrambled string "rgeat".
# 
# 
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
# 
# 
# We say that "rgeat" is a scrambled string of "great".
# 
# Similarly, if we continue to swap the children of nodes "eat" and "at", it
# produces a scrambled string "rgtae".
# 
# 
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
# 
# 
# We say that "rgtae" is a scrambled string of "great".
# 
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.
# 
# Example 1:
# 
# 
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
# 
#

# @lc code=start
class Solution:
    '''recursion, try splitting the string at all locations,
       at the splitting point, try either swap or not to swap
    '''
    def isScramble(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m != n:
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]) or f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]): # swap or no swap
                return True
        return False

# @lc code=end


'''
"abcdefghijklmnopq"
"efghijklmnopqcadb"
'''