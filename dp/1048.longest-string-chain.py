#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsdict = defaultdict(list)
        for word in words:
            wordsdict[len(word)].append(word)
        keys = list(wordsdict.keys())
        dp = {'': 0}
        ans = 0
        for length in range(min(keys), max(keys)+1):
            new_dp = {}
            for word in wordsdict[length]:
                new_dp[word] = 1            # word can be the beginning of a new chain
                for i in range(length):
                    remove_i = word[:i] + word[i+1:]
                    if remove_i in dp:
                        new_dp[word] = max(new_dp[word], dp[remove_i] + 1)
                ans = max(ans, new_dp[word])
            dp = new_dp
        return ans





# @lc code=end

