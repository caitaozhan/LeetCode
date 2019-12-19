#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.69%)
# Likes:    6031
# Dislikes: 347
# Total Accepted:    1M
# Total Submissions: 3.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        char_2_index = {s[0]:0}
        maxx = 1
        j = 0                      # j is left index of the substring
        for i in range(1, len(s)): # i is right index of substring
            if s[i] in char_2_index:
                index = char_2_index[s[i]]
                for k in range(j, index + 1):  # delete
                    char_2_index.pop(s[k])
                j = index + 1
            char_2_index[s[i]] = i
            maxx = max(maxx, i - j + 1)
        
        return maxx


class Solution:
    '''improve: without using pop()
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        char_2_index = {s[0]:0}
        maxx = 1
        start = 0                     # start is left index of the substring
        for i in range(1, len(s)):    # i is right index of substring
            if s[i] in char_2_index and char_2_index[s[i]] >= start:
                start = char_2_index[s[i]] + 1
            char_2_index[s[i]] = i
            maxx = max(maxx, i - start + 1)
        
        return maxx

# @lc code=end

