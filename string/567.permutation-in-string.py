#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

from collections import Counter

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter = Counter(s1)
        N = len(s1)
        if N > len(s2):
            return False
        s2counter = Counter(s2[:N])
        if s1counter == s2counter:
            return True
        for i in range(N, len(s2)):
            s2counter[s2[i - N]] -= 1
            s2counter[s2[i]] += 1
            if s1counter == s2counter:
                return True
        return False


# @lc code=end

