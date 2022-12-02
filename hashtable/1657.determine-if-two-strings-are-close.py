#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

from collections import Counter

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        keys1 = set(count1.keys())
        keys2 = set(count2.keys())
        if keys1 != keys2:
            return False
        vals1 = sorted(list(count1.values()))
        vals2 = sorted(list(count2.values()))
        for v1, v2 in zip(vals1, vals2):
            if v1 != v2:
                return False
        return True
        
# @lc code=end

