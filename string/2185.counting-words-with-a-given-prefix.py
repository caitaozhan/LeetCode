#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

from typing import List

# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        length = len(pref)
        for word in words:
            if length <= len(word) and word[:length] == pref:
                counter += 1
        return counter
        
# @lc code=end

