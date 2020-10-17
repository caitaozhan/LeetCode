#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (38.52%)
# Likes:    882
# Dislikes: 307
# Total Accepted:    178.9K
# Total Submissions: 448.1K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G',
# and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful
# to identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# 
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 10^5
# s[i] is 'A', 'C', 'G', or 'T'.
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        for i in range(len(s)-10+1):  # one bug here, forgot the +1. need to be cautious
            counter[s[i:i+10]] += 1
        ans = []
        for k, v in counter.items():
            if v > 1:
                ans.append(k)
        return ans
# @lc code=end

