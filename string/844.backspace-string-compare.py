#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        new_t = []

        for ch in s:
            if ch != '#':
                new_s.append(ch)
            elif new_s:
                new_s.pop()
        
        for ch in t:
            if ch != '#':
                new_t.append(ch)
            elif new_t:
                new_t.pop()
        
        new_s = ''.join(new_s)
        new_t = ''.join(new_t)
        return True if new_s == new_t else False
        
# @lc code=end

