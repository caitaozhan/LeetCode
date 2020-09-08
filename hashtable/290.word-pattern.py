#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        
        mydic1 = {}  # pattern -> word
        mydic2 = {}  # word -> pattern
        for p, w in zip(pattern, str):
            if p not in mydic1:
                mydic1[p] = w
            else:
                if mydic1[p] != w:
                    return False
            if w not in mydic2:
                mydic2[w] = p
            else:
                if mydic2[w] != p:
                    return False
        return True
# @lc code=end

