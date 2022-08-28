#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

from collections import Counter

# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # step 1: get the candidates
        candidates = []
        str_n = str(n)
        length = len(str_n)
        for i in range(40):
            s = str(2 ** i)
            if len(s) < length:
                continue
            if len(s) > length:
                break
            candidates.append(s)

        # test the candidates
        counter_n = Counter(str_n)
        for can in candidates:
            if Counter(can) == counter_n:
                return True
        return False

        
# @lc code=end

