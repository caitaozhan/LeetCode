#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#
# @lc code=start

import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = math.floor(minutesToTest / minutesToDie)
        ans = 0
        while True:
            y = (rounds + 1) ** ans
            if y >= buckets:
                break
            ans += 1
        return ans

        
# @lc code=end

