#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (49.24%)
# Likes:    579
# Dislikes: 84
# Total Accepted:    14.4K
# Total Submissions: 27.7K
# Testcase Example:  '"bcabc"'
#
# Return the lexicographically smallest subsequence of s that contains all the
# distinct characters of s exactly once.
# 
# Note: This question is the same as 316:
# https://leetcode.com/problems/remove-duplicate-letters/
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start

from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # find pos - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        if not s:
            return ''
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: 
                pos = i
            c[s[i]] -=1
            if c[s[i]] == 0:   # idea: if no duplicates for s[i], then the smallest char before index i must be in the final solution
                break
        # our answer is the leftmost letter plus the recursive call on the remainder of the string
        # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
        return s[pos] + self.smallestSubsequence(s[pos:].replace(s[pos], ""))


def test():
    # string = 'cbacdcbc'
    string = 'bccab'
    s = Solution()
    print(s.smallestSubsequence(string))

test()
# @lc code=end

