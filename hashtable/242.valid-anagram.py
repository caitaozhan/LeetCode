#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

from collections import Counter

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter()
        counter2 = Counter()
        for ch in s:
            counter1[ch] += 1
        for ch in t:
            counter2[ch] += 1
        return counter1 == counter2
        
# @lc code=end

