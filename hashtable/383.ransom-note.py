#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

from collections import Counter

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        for key, val in counter1.items():
            if val > counter2[key]:
                return False
        return True
        
# @lc code=end

