#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

from collections import Counter

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occur = set()
        for _, val in count.items():
            if val in occur:
                return False
            else:
                occur.add(val)
        return True
        
# @lc code=end

