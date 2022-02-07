#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution1:
    '''using sort'''
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        for key, val in counter_t.items():
            if counter_s[key] != val:
                return key

# @lc code=end

