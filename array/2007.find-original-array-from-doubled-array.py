#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort(reverse=True)
        counter = Counter(changed)
        ans = []
        for num in changed:
            if counter[num] == 0:
                continue
            if num % 2 == 1:
                break
            half = num // 2
            if counter[half] == 0:
                break
            ans.append(half)
            counter[num] -= 1
            counter[half] -= 1
        else:
            return ans
        return []

changed = [1,3,6,8,4,2]
changed = [6,3,0,2]
s = Solution()
print(s.findOriginalArray(changed))

        
# @lc code=end

