#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

from collections import Counter
from curses.ascii import SO

# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        freqs = sorted(counter.values(), key=lambda x: -x)
        max_freq = freqs[0]
        ans = 0
        for i in range(1, len(freqs)):
            if freqs[i] < max_freq:
                max_freq = freqs[i]
            else:
                if max_freq == 0:
                    ans += freqs[i]   # delete all
                else:
                    ans += (freqs[i] - max_freq + 1)
                    max_freq = max_freq - 1
        return ans


string = "beaddedbacdcd"
s = Solution()
print(s.minDeletions(string))


# @lc code=end

