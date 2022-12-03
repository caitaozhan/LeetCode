#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

from collections import Counter

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = []
        for key, val in sorted(count.items(), key=lambda x: x[1], reverse=True):
            ans.append(key * val)
        return ''.join(ans)
        
# @lc code=end

