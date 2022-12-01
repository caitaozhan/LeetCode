#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

from collections import Counter

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        c1 = Counter(s[:n//2])
        c2 = Counter(s[n//2:])
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        num1 = 0
        for ch in vowels:
            num1 += c1[ch]
        num2 = 0
        for ch in vowels:
            num2 += c2[ch]
        return num1 == num2


        
# @lc code=end

